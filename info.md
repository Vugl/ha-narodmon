{% if prerelease %}
### NB!: This is a Beta version!
{% endif %}

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![hacs][hacs-shield]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![Support me on Patreon][patreon-shield]][patreon]

[![Community Forum][forum-shield]][forum]

_Component to integrate with Narodmon cloud and automatic search for the nearest sensors of the required type._

![Narodmon Logo](narodmon-logo.png)

## Known Limitations and Issues

- At the moment, configuring the component is only possible through `configuration.yaml`. Support for configuration via Home Assistant UI will be added in the future.

## Features:

- Automatically selects the closest sensor of the required type.
- If the sensor becomes unavailable, it automatically switches to the new nearest sensor.
- Allows you to easily configure sensor groups for different locations.

{% if not installed %}
## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Narodmon".

{% endif %}
## Configuration is done in the UI

<!---->

## Useful Links

- [Documentation][component]
- [Report a Bug][report_bug]
- [Suggest an idea][suggest_idea]

<p align="center">* * *</p>
I put a lot of work into making this repo and component available and updated to inspire and help others! I will be glad to receive thanks from you — it will give me new strength and add enthusiasm:
<p align="center"><a href="https://www.patreon.com/join/limych?" target="_blank"><img src="http://khrolenok.ru/support_patreon.png" alt="Patreon" width="250" height="48"></a></p>

| Bitcoin                                                                                                                                                                                                                  | Ethereum                                                                                                                         | Monero                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href="https://sochain.com/address/BTC/16yfCfz9dZ8y8yuSwBFVfiAa3CNYdMh7Ts" target="_blank"><img alt="Bitcoin" src="http://khrolenok.ru/support_btc.png" width="200"/></a><pre>16yfCfz9dZ8y8yuSwBFVfiAa3CNYdMh7Ts</pre> | <img alt="Ethereum" src="http://khrolenok.ru/support_eth.png" width="200"/><pre>0x9FB9429f9A85Fa2395Bb59e50452F64977435d61</pre> | <img alt="Monero" src="http://khrolenok.ru/support_xmr.png" width="200"/><pre>48Kt2ksKYxHg46T5sJ7feBXtndHhxk1JgYJwtwGG8Jb7asNFShRwUDtFgX2UvVThXa5GGyGbMCfNJX7YwFZBRDX43q4mT83</pre> |

***

[component]: https://github.com/Limych/ha-narodmon
[commits-shield]: https://img.shields.io/github/commit-activity/y/Limych/ha-narodmon.svg?style=popout
[commits]: https://github.com/Limych/ha-narodmon/commits/dev
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=popout
[hacs]: https://hacs.xyz
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[forum]: https://community.home-assistant.io/t/narodmon-cloud-integration/285737
[license]: https://github.com/Limych/ha-narodmon/blob/main/LICENSE.md
[license-shield]: https://img.shields.io/badge/license-Creative_Commons_BY--NC--SA_License-lightgray.svg?style=popout
[maintenance-shield]: https://img.shields.io/badge/maintainer-Andrey%20Khrolenok%20%40Limych-blue.svg?style=popout
[releases-shield]: https://img.shields.io/github/release/Limych/ha-narodmon.svg?style=popout
[releases]: https://github.com/Limych/ha-narodmon/releases
[releases-latest]: https://github.com/Limych/ha-narodmon/releases/latest
[user_profile]: https://github.com/Limych
[report_bug]: https://github.com/Limych/ha-narodmon/issues/new?template=bug_report.md
[suggest_idea]: https://github.com/Limych/ha-narodmon/issues/new?template=feature_request.md
[contributors]: https://github.com/Limych/ha-narodmon/graphs/contributors
[patreon-shield]: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3DLimych%26type%3Dpatrons&style=popout
[patreon]: https://www.patreon.com/join/limych
