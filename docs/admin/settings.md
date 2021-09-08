---
title: InvenTree Admin Settings
---

## Admin Settings

InvenTree ships with a lot of dynmaic settings. While [config file settings](../start/config.md) require access to the webserver on which InvenTree is hosted these can be changed by all admins of the server.

### User Settings

Change how InvenTree apears to the individual user and configure login and user data.

### Global Settings

#### Login Settings

Change how logins, password-forgt, signups are handled.

| Settings Name | Type | Description | Default |
| --- | --- | --- | --- |
| Enable registration | True/False | Enable self-registration for users on the login-pages | False |
| Enable SSO | True/False | Enable SSO on the login-pages | False |
| Enable password forgot | True/False | Enable password forgot function on the login-pages.<br><br>This will let users reset their passwords on their own. For this feature to work you need to configure E-mail | True |
| E-Mail required | True/False | Require user to supply e-mail on signup.<br><br>Without a way (e-mail) to contact the user notifications and security features might not work! | False |
| Mail twice | True/False | On signup ask users twice for their mail | False |
| Password twice | True/False | On signup ask users twice for their password | True |
| Auto-fill SSO users | True/False | Automatically fill out user-details from SSO account-data.<br><br>If this feature is enabled the user is only asked for their username, first- and surname if those values can not be gathered from their SSO profile. This might lead to unwanted usernames bleading over. | True |
