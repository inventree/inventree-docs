---
title: Pricing
---

## Pricing

InvenTree provides multi-currency pricing support via the [django-money](https://django-money.readthedocs.io/en/latest/) library.

## Currency Conversion

Automatic updating of currency conversion rates can be provided via the [exchangerate.host](https://exchangerate.host/#/) API.

Currency exchange rates are updated once per day.

The rates can also be set manually in the settings. Be aware that most companies trade with hourly or daily rates – setting a static rate can lead to big differences to the real world.
