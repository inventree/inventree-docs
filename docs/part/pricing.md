---
title: Pricing
---

## Pricing

InvenTree provides multi-currency pricing support via the [django-money](https://django-money.readthedocs.io/en/latest/) library.

## Currency Conversion

If multiple currency support is required, automatic updating of currency conversion rates can be provided via the [fixer.io](https://fixer.io) API.

If a valid API key for the fixer.io service is provided, the InvenTree background worker will update the currency exchanges rates once per day.

### API Key

A free API key can be obtained by creating an account with fixer.io. 