---
title: Return Order
---

## Return Orders

Return Orders allow stock items (which have been sold or allocted to a customer) to be to be returned into stock, typically for the purpose of repair or refund.

!!! tip "An Order By Any Other Name"
    A Return Order may also be known as an [RMA](https://en.wikipedia.org/wiki/Return_merchandise_authorization) 

### Enable Return Order Functionality

By default, Return Order functionality is not enabled - it must be enabled by a *staff* user from the settings page:

{% with id="enable-return-order", url="sell/return_order_enable.png", description="Enable Return Orders" %}
{% include "img.html" %}
{% endwith %}

Once this setting is enabled, you can access the "Return Orders" page from the main navigation bar:

{% with id="return-order-navbar", url="sell/return_order_navbar.png", description="Access Return Orders" %}
{% include "img.html" %}
{% endwith %}

### Return Order Reference

Each Return Order is uniquely identified by its *Reference* field. Read more about [reference fields](../settings/reference.md).
