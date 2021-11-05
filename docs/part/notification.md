---
title: Part Notifications
---

## Notifications

Users can select to receive email notifications when certain events occur.

!!! warning "Email Configuration Required"
    Notifications require correct [email configuration](../../start/config/#email-settings)

!!! warning "Valid Email Address"
    Each user must have a valid email address associated with their account to receive email notifications

### Low Stock Notification

If the *minimum stock* threshold is set for a *Part*, then a "low stock" notification can be generated when the stock level for that part falls below the configured level.

Any users who are subscribed to notifications for the part in question will receive a low stock notification via email.

### Build Order Notification

When a new [Build Order](../../build/build/) is created, the InvenTree software checks to see if any of the parts required to complete the order are low on stock.

If there are any parts with low stock, a notification is generated for any users subscribed to notifications for the part being built.

## Subscribing to Notifications

Users can "subscribe" to either a *Part* or *Part Category*, to receive notifications.

### Part

When subscribed to a *Part*, a user will receive notifications when events occur which pertain to:

- That particular part
- Any variant parts

If a user is subscribed to a particular part, it will be indicated as shown below:

{% with id="part_sub_on", url="part/part_subscribe_on.png", description="Subscribe" %}
{% include 'img.html' %}
{% endwith %}

If the user is not subscibed, the subscription icon is greyed out, as shown here:

{% with id="part_sub_off", url="part/part_subscribe_off.png", description="Subscribe" %}
{% include 'img.html' %}
{% endwith %}

Clicking on this icon will toggle the subscription status for this part.

### Part Category

When subscribed to a *Part Category*, a user will receive notifications when particular events occur which pertain to:

- That particular category
- Any sub-categories at lower levels
- Any parts contained in the category
- Any parts contained in the lower level categories

Subscribing to a part category operates in the same manner as for a part - simply click on the notification icon:

{% with id="cat_sub", url="part/category_notification.png", description="Subscribe to part category" %}
{% include 'img.html' %}
{% endwith %}
