---
title: InvenTree Single Sign On
---

## Single Sign On

InvenTree provides the possibility to use 3rd party services to authenticate users. This functionality makes use of [django-allauth](https://django-allauth.readthedocs.io/en/latest/) and supports a wide array of OpenID and OAuth [provider](https://django-allauth.readthedocs.io/en/latest/providers.html).

### Configuration

To use SSO you have to:

1. Enable the required providers in the [config file](../start/config.md#Single-Sign-on).
1. Add the required client configurations in the `SocialApp` app in the [admin interface](../settings/admin.md).
1. Enable SSO for the users in the [global settings](../settings/global.md).
1. Configure [e-mail](../settings/email.md).

### Security Consideration

You should use SSL for your website if you want to use this feature. Also set your callback-endpoints to `https://` addresses to reduce the risk of leaking user's tokens.

Tokens for authenticating the users to the providers they registered with are saved in the database.  
So ensure your database is protected and not open to the internet.  
Make sure all users with admin privileges have sufficient passwords - they can read out your client configurations with providers and all auth-tokens from users.

!!! warning "It's a secret!"
    Never share your installs secret key!
