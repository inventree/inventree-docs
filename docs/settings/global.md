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

Configuration of basic server settings.

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| InvenTree Instance Name | String | String descriptor for the InvenTree server instance | InvenTree Server |
| Use Instance Name | Boolean | Use instance name in title bars | False |
| Base URL | String | Base URL for server instance | *blank* |
| Company Name | String | Company name | My compant name |
| Download from URL | Boolean | Allow downloading of images from remote URLs | False |

### Login Settings

Change how logins, password-forgot, signups are handled.

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Enable registration | Boolean | Enable self-registration for users on the login-pages | False |
| Enable SSO | Boolean | Enable SSO on the login-pages | False |
| Enable password forgot | Boolean | Enable password forgot function on the login-pages.<br><br>This will let users reset their passwords on their own. For this feature to work you need to configure E-mail | True |
| E-Mail required | Boolean | Require user to supply e-mail on signup.<br><br>Without a way (e-mail) to contact the user notifications and security features might not work! | False |
| Enforce MFA | Boolean | Users must use multifactor security.<br><br>This forces each user to setup MFA and use it on each autentication | False |
| Mail twice | Boolean | On signup ask users twice for their mail | False |
| Password twice | Boolean | On signup ask users twice for their password | True |
| Auto-fill SSO users | Boolean | Automatically fill out user-details from SSO account-data.<br><br>If this feature is enabled the user is only asked for their username, first- and surname if those values can not be gathered from their SSO profile. This might lead to unwanted usernames bleading over. | True |

### Barcodes

Configuration of barcode functionality

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Barcode Support | Boolean | Enable barcode functionality in web interface | True |

### Currencies

Configuration of currency support

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Default Currency | Currency | Default currency | USD | 

### Reporting

Configuration of report generation

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Enable Reports | Boolean | Enable report generation | False |
| Page Size | String | Default page size | A4 |
| Debug Mode | Boolean | Generate reports in debug mode (HTML output) | False |
| Test Reports | Boolean | Enable generation of test reports | False |

### Parts

Configuration of Part options

### Categories

Configuration of Part Category options

### Stock

Configuration of Stock Item options

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Stock Expiry | Boolean | Enable stock expiry functionality | False |
| Stock Stale Time | Days | Number of days stock items are considered stale before expiring | 90 |
| Sell Expired Stock | Boolean | Allow sale of expired stock | False |
| Build Expired Stock | Boolean | Allow building with expired stock | False |
| Stock Ownership Control | Boolean | Enable ownership control functionality | False |

### Build Orders

Options for build orders

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Reference Prefix | String | Prefix for build order reference | BO |
| Reference Regex | String | Regular expression pattern for build order reference | *blank* |

### Purchase Orders

Options for purchase orders

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Reference Prefix | String | Prefix for purchase order reference | PO |


### Sales orders

Options for sales orders

| Setting | Type | Description | Default |
| --- | --- | --- | --- |
| Reference Prefix | String | Prefix for sales order reference | SO |
