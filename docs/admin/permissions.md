---
title: User Permissions
---

## Permissions

!!! warning "TODO"
    This section requires further work - in particular screenshots!

InvenTree provides a permission system which allows authority control on a user or group basis.

!!! info "Django Permissions"
    InvenTree implements the django permissions system. For background reading, refer to the [django permissions documentation](https://docs.djangoproject.com/en/3.1/topics/auth/default/#permissions-and-authorization).

Permissions can be assigned for each model in the InvenTree database. The following permission classes are available for each model (or "table") in the database:

### View

Users with the *View* permission for a particular model will be able to view data associated with the model.

*For example, a user who has the View permission set for the PurchaseOrder model will be able to view purchase orders.*

### Add

Users with the *Add* permission for a particular model will be able to add (create) new instances of that model.

*For example, a user who has the Add permission set for the StockItem model will be able to add / create new stock item objects.*

### Edit

Users with the *Edit* permissions for a particular model will be able to edit (adjust) instances of that model.

*For example, a user who has the Edit permission set for the Build model will be able to edit Build items.*

### Delete

Users with the *Delete* permission for a particular model will be able to delete instances of that model.

## Superuser Account

The *superuser* account (normally the first user created when configuring the database) automatically has every assigned permission.

## Assigning Permissions

The *superuser* account can assign model permissions to any users or groups.

Additionally, any users who have permissions to edit the *Users* table can also adjust these permissions.

### User Permissions

User permissions allow model permissions to be assigned on a single user basis. This is useful if you wish to finely control which InvenTree features a certain user can access.

### Group Permissions

Group permissions allow model permissions to be assigned to a *group* of users which greatly simplifies the task of assigning similar permissions to multiple users.

## Admin Interface Permissions

If a user does not have the required permissions to perform a certain action in the admin interface, those options not be displayed.

If a user is expecting a certain option to be available in the admin interface, but it is not present, it is most likely the case that the user does not have those permissions assigned. 

## Web Interface Permissions

When using the InvenTree web interface, certain functions may not be available for a given user, depending on their permissions. In this case, user-interface elements may be disabled, or may be removed.

## API Permissions

When using the InvenTree API, certain endpoints or actions may be inaccessible for a given user, depending on their permissions.

As the API is used extensively within the web interface, this means that many data tables may also be impacted by user permissions.
