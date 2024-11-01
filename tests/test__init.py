"""Tests for Narodmon Cloud Integration component."""

import logging
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.setup import async_setup_component
from voluptuous import Invalid

from custom_components.narodmon import (
    CONF_APIKEY,
    DOMAIN,
    YAML_DOMAIN,
    NarodmonDataUpdateCoordinator,
    async_setup_entry,
    cv_apikey,
)
from custom_components.narodmon.api import NarodmonApiClient


async def test_cv_apikey():
    """Test API keys verification."""
    # Valid keys
    for apikey in [
        "B46CD5A6B1BC28E3D",
        "d41d8cd98f00b204e9800998ecf8427e",
        "iTkToPPq6SFMOvM7kkcBxmHRcHsOVpVN",
        "e852o0eK4DSEoImMsWoLDIpyB4g02iC486P9pY9b8WqJhmiwJBJqEUUgpRLB0z",
        "MujSTK",
    ]:
        assert cv_apikey(apikey)

    # Invalid keys
    for apikey in [
        "B46CD5A6B1BC28E3D+",
        "=0b204e9800998ecf",
        '2Q*j>*Q%ppgOK"~W',
        123,
        b"B46CD5A6B1BC28E3D",
    ]:
        with pytest.raises(Invalid):
            cv_apikey(apikey)


async def test_setup(hass: HomeAssistant, yaml_config, caplog):
    """Test setup from configuration.yaml."""
    with (
        patch.object(
            NarodmonApiClient,
            "async_init",
            new_callable=AsyncMock,
        ),
        patch.object(
            NarodmonApiClient,
            "async_update_data",
            new_callable=AsyncMock,
            return_value={},
        ),
        caplog.at_level(logging.WARNING),
    ):
        assert await async_setup_component(hass, DOMAIN, yaml_config)
        await hass.async_block_till_done()
        assert len(hass.states.async_all()) == 2
        assert len(caplog.records) == 1


async def test_setup_apikey(hass: HomeAssistant, yaml_config, caplog):
    """Test setup from configuration.yaml."""
    with (
        patch.object(
            NarodmonApiClient,
            "async_init",
            new_callable=AsyncMock,
        ),
        patch.object(
            NarodmonApiClient,
            "async_update_data",
            new_callable=AsyncMock,
            return_value={},
        ),
        caplog.at_level(logging.WARNING),
    ):
        yaml_config[DOMAIN][CONF_APIKEY] = "testapikey"
        assert await async_setup_component(hass, DOMAIN, yaml_config)
        await hass.async_block_till_done()
        assert len(hass.states.async_all()) == 2
        assert len(caplog.records) == 2


# We can pass fixtures as defined in conftest.py to tell pytest to use the fixture
# for a given test. We can also leverage fixtures and mocks that are available in
# Home Assistant using the pytest_homeassistant_custom_component plugin.
# Assertions allow you to verify that the return value of whatever is on the left
# side of the assertion matches with the right side.
async def test_setup_unload_and_reload_entry(
    hass: HomeAssistant, yaml_config, config_entry, bypass_get_data
):
    """Test entry setup and unload."""
    config_entry.add_to_hass(hass)
    hass.data.setdefault(YAML_DOMAIN, {})
    hass.data[YAML_DOMAIN] = yaml_config[DOMAIN]

    # Set up the entry and assert that the values set during setup are where we expect
    # them to be. Because we have patched the
    # NarodmonDataUpdateCoordinator.async_get_data call, no code from
    # custom_components/narodmon/api.py actually runs.
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()
    #
    assert DOMAIN in hass.data
    assert config_entry.entry_id in hass.data[DOMAIN]
    cfg = hass.data[DOMAIN][config_entry.entry_id]
    assert isinstance(cfg, dict)
    for item in cfg.values():
        assert isinstance(item, NarodmonDataUpdateCoordinator)

    # Reload the entry and assert that the data from above is still there
    await hass.config_entries.async_reload(config_entry.entry_id)
    await hass.async_block_till_done()
    #
    assert DOMAIN in hass.data
    assert config_entry.entry_id in hass.data[DOMAIN]
    cfg = hass.data[DOMAIN][config_entry.entry_id]
    assert isinstance(cfg, dict)
    for item in cfg.values():
        assert isinstance(item, NarodmonDataUpdateCoordinator)

    # Unload the entry and verify that the data has been removed
    await hass.config_entries.async_unload(config_entry.entry_id)
    await hass.async_block_till_done()
    #
    assert config_entry.entry_id not in hass.data[DOMAIN]


async def test_setup_entry_exception(
    hass: HomeAssistant, yaml_config, config_entry, error_on_get_data
):
    """Test ConfigEntryNotReady when API raises an exception during entry setup."""
    config_entry.add_to_hass(hass)
    hass.data.setdefault(YAML_DOMAIN, {})
    hass.data[YAML_DOMAIN] = yaml_config[DOMAIN]

    # In this case we are testing the condition where async_setup_entry raises
    # ConfigEntryNotReady using the `error_on_get_data` fixture which simulates
    # an error.
    with pytest.raises(ConfigEntryNotReady):
        assert await async_setup_entry(hass, config_entry)
