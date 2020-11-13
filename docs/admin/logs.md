---
title: Admin Shell
---

## Error Logs

Any critical server error logs are recorded to the database, and can be viewed by staff users using the admin interface.

In the admin interface, select the "Errors" view:

{% with id="admin_error_link", url="admin/admin_errors_link.png", description="Admin errors" %}
{% include 'img.html' %}
{% endwith %}

!!! note "URL"
    Alternatively, navigate to the error list view at /admin/error_report/error/

A list of error logs is presented.

{% with id="admin_error_logs", url="admin/admin_errors.png", description="Error logs" %}
{% include 'img.html' %}
{% endwith %}

!!! note "Deleting Logs"
    Error logs should be deleted periodically