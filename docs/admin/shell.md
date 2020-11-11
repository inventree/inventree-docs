---
title: Admin Shell
---

## Python Shell

A Python shell interface is provided at /admin/shell/.

This interface allows advanced users direct access to the underlying database objects using Python. 

!!! warning "Danger"
    The scripting shell interface should only ever be used by advanced users. It requires intimate knowledge of the underlying InvenTree code, and improper use could easily result in corruption of data

!!! warning "Seriously"
    If you are not 100% sure of what you are doing, do not use the shell interface

!!! info "Enabling Shell Mode"
    The admin shell is (by default) only enabled when InvenTree is running in DEBUG mode

The shell interface allows Python queries to be run by the admin user, as shown below:

{% with id="admin_shell", url="admin/shell.png", description="Admin shell interface" %}
{% include 'img.html' %}
{% endwith %}