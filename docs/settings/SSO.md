---
title: InvenTree Single Sign On
---

## Single Sign On

InvenTree provides the possibility to use 3rd party services to authenticate users. This functionality makes use of [django-allauth](https://django-allauth.readthedocs.io/en/latest/) and supports a wide array of OpenID and OAuth [providers](https://django-allauth.readthedocs.io/en/latest/providers.html).

!!! tip "Provider Documentation"
    There are a lot of technical considerations when configuring a particular SSO provider. A good starting point is the [django-allauth documentation](https://django-allauth.readthedocs.io/en/latest/providers.html)

## SSO Configuration

The basic requirements for configuring SSO are outlined below:

1. Enable the required providers in the [config file](../start/config.md#single-sign-on).
1. Add the required client configurations in the `SocialApp` app in the [admin interface](../settings/admin.md).
1. Enable SSO for the users in the [global settings](../settings/global.md).
1. Configure [e-mail](../settings/email.md).

### Configuration File

The first step is to ensure that the required provider modules are installed, via your installation [configuration file](../start/config.md#single-sign-on).

There are two variables in the configuration file which define the operation of SSO:

| Key | Description | More Info |
| --- | --- | --- | 
| `social_backends` | A *list* of provider backends enabled for the InvenTree instance | [django-allauth docs](https://django-allauth.readthedocs.io/en/latest/installation.html) |
| `social_providers` | A *dict* of settings specific to the installed providers | [provider documentation](https://django-allauth.readthedocs.io/en/latest/providers.html) |

In the example below, SSO provider modules are activated for *google*, *github* and *microsoft*. Specific configuration options are specified for the *microsoft* provider module:

{% with id="SSO", url="settings/sso_config.png", description="SSO Config" %}
{% include 'img.html' %}
{% endwith %}

!!! info "Provider Module Format"
    Note that the provider modules specified in `social_backends` must be prefixed with `allauth.socialaccounts.providers`

### Add Client Configurations

### Enable SSO Settings

### Configure Email

Note that [email settings](./email.md) must be correctly configured before SSO will be activated. Ensure that your email setup is correctly configured and operataional.

## Security Consideration

You should use SSL for your website if you want to use this feature. Also set your callback-endpoints to `https://` addresses to reduce the risk of leaking user's tokens.

Tokens for authenticating the users to the providers they registered with are saved in the database.  
So ensure your database is protected and not open to the internet.  

Make sure all users with admin privileges have sufficient passwords - they can read out your client configurations with providers and all auth-tokens from users.

!!! warning "It's a secret!"
    Never share the secret key associated with your InvenTree install!
