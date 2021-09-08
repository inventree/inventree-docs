---
title: Database Configuration
---

## Database Configuration

Admin users will need to adjust the InvenTree installation to meet the particular needs of their setup. For example, pointing to the correct database backend, or specifying a list of allowed hosts.

InvenTree system settings can be specified in a configuration file, or via environment variables.

!!! info "Environment Variables"
    Settings specified using environment variables take priority

### Configuration File

To support install specific settings, a simple configuration file ``config.yaml`` is provided. This configuration file is loaded by the InvenTree server at runtime. Settings specific to a given install should be adjusted in ``config.yaml``.

The default InvenTree config file is located at `./InvenTree/config.yaml`

However, the config file can be placed elsewhere, and specified with the `INVENTREE_CONFIG_FILE` environment variable.

The default configuration file file is shown below:

``` yaml
{% include 'config.yaml' %}
```

### Environment Variables

In addition to specifying InvenTree options via the `config.yaml` file, these options can also be specified via environment variables. This can be usful for system administrators who want the flexibility of altering settings without editing the configuration file.

- Environment variable settings use the `INVENTREE_` prefix, and are all uppercase.
- Config file settings do not use this prefix, and are all lowercase

!!! info Priotity
    Configuration options set via environment variables will take priority over the values set in the `config.yaml` file.

!!! warning Available Variables
    Some configuration options cannot be set via environment variables. Refer to the documentation below.

## Basic Options

The following basic options are available:

| Environment Variable | Settings File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DEBUG | debug | Enable debug mode | True |
| INVENTREE_LOG_LEVEL | log_level | Set level of logging to terminal | WARNING |

## Secret Key

InvenTree requires a secret key for providing cryptographic signing - this should be a secret (and unpredictable) value.

The secret key can be provided in multiple ways, with the following (descending) priorities:

**Pass Secret Key via Environment Variable**

A secret key string can be passed directly using the environment variable `INVENTREE_SECRET_KEY`

**Pass Secret Key File via Environment Variable**

A file containing the secret key can be passed via the environment variable `INVENTREE_SECRET_KEY_FILE`

**Fallback to Default Secret Key File**

If not specified via environment variables, the fallback secret_key file (automatically generated as part of InvenTree installation) will be used.

## Database Options

InvenTree provides support for multiple database backends - any backend supported natively by Django can be used. 

Database options are specified under the *database* heading in the configuration file. Any option available in the Django documentation can be used here - it is passed through transparently to the management scripts.

The following database options can be configured:

| Environment Variable | Settings File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DB_ENGINE | database.ENGINE | Database backend | *Not set* |
| INVENTREE_DB_NAME | database.NAME | Database name | *Not set* |
| INVENTREE_DB_USER | database.USER | Database username (if required) | *Not set* |
| INVENTREE_DB_PASSWORD | database.PASSWORD | Database password (if required) | *Not set* |
| INVENTREE_DB_HOST | database.HOST | Database host address (if required) | *Not set* |
| INVENTREE_DB_PORT | database.PORT | Database host port (if required) | *Not set* |

## Email Settings

To enable [email functionality](../admin/email.md), email settings must be configured here, either via environment variables or within the configuration file.

The following email settings are available:

| Environment Variable | Settings File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_EMAIL_BACKEND | email.backend | Email backend module | django.core.mail.backends.smtp.EmailBackend |
| INVENTREE_EMAIL_HOST | email.host | Email server host | *Not set* |
| INVENTREE_EMAIL_PORT | email.port | Email server port | 25 |
| INVENTREE_EMAIL_USERNAME | email.username | Email account username | *Not set* |
| INVENTREE_EMAIL_PASSWORD | email.password | Email account password | *Not set* |
| INVENTREE_EMAIL_TLS | email.tls | Enable TLS support | False |
| INVENTREE_EMAIL_SSL | email.ssl | Enable SSL support | False |
| INVENTREE_EMAIL_SENDER | email.sender | Name of sender | *Not set* |

## Allowed Hosts / CORS

By default, all hosts are allowed, and CORS requests are enabled from any origin. **This is not secure and should be adjusted for your installation**. These options can be changed in the configuration file.

For further information, refer to the following documentation:

* [Django ALLOWED_HOSTS](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts)
* [Django CORS headers](https://github.com/OttoYiu/django-cors-headers)

## File Storage Locations

### Static File Storage

By default, static files are stored in the local directory `/home/inventree/static`. This directory should be changed by specifying the `static_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_STATIC_ROOT` environment variable.

### Uploaded File Storage

By default, uploaded media files are stored in the local directory `/home/inventree/media`. This directory should be changed by specifying the `media_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_MEDIA_ROOT` environment variable.

## Authentication

### Single Sign on


### Login Options

The login-experience can be altered with the following settings:
| Environment Variable | Settings File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_LOGIN_CONFIRM_DAYS | login_confirm_days | Duration for which confirmation links are valid | 3 |
| INVENTREE_LOGIN_ATTEMPTS | login_attempts | Count of allowed login attempts before blocking user | 5 |

### Authentication Backends

Custom authentication backends can be used by specifying them here

## Other Options

### Middleware

Custom middleware layers can specified here.