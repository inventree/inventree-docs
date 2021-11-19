---
title: Global Settings
---

## Global Settings

InvenTree ships with a lot of dynamic settings which can be configured at run-time. These settings are stored in the InvenTree database itself.

The following settings are *global* settings which affect all users. 

!!! info "Staff Status Required"
    Only users with *staff* status can view and edit global settings

To edit global settings, select *Settings* from the menu in the top-right corner of the screen.

Global settings are arranged in the following categories:

### Server Settings

Configuration of basic server settings

### Login Settings

Change how logins, password-forgot, signups are handled.

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Enable registration | Boolean | Enable self-registration for users on the login-pages | False |
| Enable SSO | Boolean | Enable SSO on the login-pages | False |
| Enable password forgot | Boolean | Enable password forgot function on the login-pages.<br><br>This will let users reset their passwords on their own. For this feature to work you need to configure E-mail | True |
| E-Mail required | Boolean | Require user to supply e-mail on signup.<br><br>Without a way (e-mail) to contact the user notifications and security features might not work! | False |
| Mail twice | Boolean | On signup ask users twice for their mail | False |
| Password twice | Boolean | On signup ask users twice for their password | True |
| Auto-fill SSO users | Boolean | Automatically fill out user-details from SSO account-data.<br><br>If this feature is enabled the user is only asked for their username, first- and surname if those values can not be gathered from their SSO profile. This might lead to unwanted usernames bleading over. | True |

### Barcodes

Configuration of barcode functionality

### Currencies

Configuration of currency support

### Reporting

Configuration of report generation

### Parts

Configuration of Part options

### Categories

Configuration of Part Category options

### Stock

Configuration of Stock Item options

### Build Orders

Options for build orders

### Purchase Orders

Options for purchase orders

### Sales orders

Options for sales orders