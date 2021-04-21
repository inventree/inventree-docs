---
title: Contributing to InvenTree
---

## Contribute to InvenTree

InvenTree is an open source project, and benefits greatly from user contributions.

If you find InvenTree to be useful, and wish to improve the software, please consider contributing:

### Source Code

InvenTree is built using [Python3](https://www.python.org/) and [Django](https://www.djangoproject.com/). Source code is available on [GitHub](https://github.com/inventree/inventree).

Contributions towards the core InvenTree code base are welcomed; either extending current functionality, prodiving new features, or addressing outstanding issues.

### Report Bugs

If you find a bug or a feature that does not work correctly, please report it on [GitHub](https://github.com/inventree/inventree/issues). Reporting bugs is critical to improving the software. If you are able and willing, providing a fix for any outstanding issues would be greatly appreciated.

### Translation

![de translation](https://img.shields.io/badge/dynamic/json?color=blue&label=de&style=flat&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)
![fr translation](https://img.shields.io/badge/dynamic/json?color=blue&label=fr&style=flat&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)
![it translation](https://img.shields.io/badge/dynamic/json?color=blue&label=it&style=flat&query=%24.progress.4.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)
![pl translation](https://img.shields.io/badge/dynamic/json?color=blue&label=pl&style=flat&query=%24.progress.5.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)
![ru translation](https://img.shields.io/badge/dynamic/json?color=blue&label=ru&style=flat&query=%24.progress.6.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)
![zh-CN translation](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&query=%24.progress.7.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-14720186-452300.json)

InvenTree provides a translation layer for the web interface, this requires effort from translators to provide multi-lingual support. If you wish to translate InvenTree to a new language (or improve an existing translation), such contributions would be greatly appreciated!.

Native language translation of the InvenTree web application is [community contributed via crowdin](https://crowdin.com/project/inventree). **Contributions are welcomed and encouraged**.

To contribute to the translation effort, navigate to the [InvenTree crowdin project](https://crowdin.com/project/inventree), create a free account, and start making translations suggestions for your language of choice!

### Documentation

Documenting a large software project is a challenging and ongoing effort. If you are able to provide assistance in improving this documentation set, please consider doing so! Documentation contributions can be made on [GitHub](https://github.com/inventree/inventree-docs).

### Donate

{% if 'readthedocs.org' in config.docs_dir %}
{% set assets = '/en/latest/assets' %}
{% else %}
{% set assets = '/assets' %}
{% endif %}

If you are unable to provide contributions as listed above, or you find InvenTree to be useful, please consider donating to support its ongoing development.

[ Donate <span class='fas fa-smile'></span> ](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=T4M976M5URSUE&currency_code=AUD){: .md-button .md-button--primary }
<img src="{{ assets }}/paypal-logo-small-min-300x136.png" border="0" alt="PayPal Logo" style="width: 136px; length:300px; vertical-align:middle; padding-left: 20px">
