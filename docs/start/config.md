---
title: Database Configuration
---

## Database Configuration

While many InvenTree options can be configured at "run time", there are a number of system configuration parameters which need to be set *before* running InvenTree. Admin users will need to adjust the InvenTree installation to meet the particular needs of their setup. For example, pointing to the correct database backend, or specifying a list of allowed hosts.

InvenTree system settings can be specified either via environment variables, or in a configuration file.

!!! info "Environment Variables"
    Settings specified using environment variables take priority. Values provided in the configuration file are ignored if a matching environment variable is present.

### Environment Variables

In addition to specifying InvenTree options via the `config.yaml` file, these options can also be specified via environment variables. This can be usful for system administrators who want the flexibility of altering settings without editing the configuration file.

Environment variable settings generally use the `INVENTREE_` prefix, and are all uppercase.

!!! info "Configuration Priority"
    Configuration options set via environment variables will take priority over the values set in the `config.yaml` file.

!!! warning "Available Variables"
    Some configuration options cannot be set via environment variables. Refer to the documentation below.

### Configuration File

To support install specific settings, a simple configuration file `config.yaml` is provided. This configuration file is loaded by the InvenTree server at runtime. Settings specific to a given install should be adjusted in `config.yaml`.

#### Configuration File Location

The InvenTree server tries to locate the `config.yaml` configuration file on startup, in the following locations:

1. Location is specified by the `INVENTREE_CONFIG_FILE` environment variable
2. Located in the same local directory as the InvenTree source code

!!! tip "Config File Location"
    When the InvenTree server boots, it will report the location where it expects to find the configuration file

The configuration file *template* can be found on [GitHub](https://github.com/inventree/InvenTree/blob/master/InvenTree/config_template.yaml) 

!!! info "Template File"
    The default configuration file (as defined by the template linked above) will be copied to the specifed configuration file location on first run, if a configuration file is not found in that location.

!!! tip "Restart Server"
    The contents of the configuration file are read when the InevnTree server first launches. If any changes are made to the configuration file, ensure that the server is restarted, so that the changes can be made operational.

## Basic Options

The following basic options are available:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DEBUG | debug | Enable [debug mode](./intro.md#debug-mode) | True |
| INVENTREE_LOG_LEVEL | log_level | Set level of logging to terminal | WARNING |
| INVENTREE_TIMZONE | timezome | Server timezone | UTC |
| ADMIN_URL | admin_url | URL for accessing [admin interface](../settings/admin.md) | admin |
| INVENTREE_LANGUAGE | language | Default language | en-us |

## Administrator Account

An administrator account can be specified using the following environment variables:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_ADMIN_USER | admin_user | Admin account username | *Not set* |
| INVENTREE_ADMIN_PASSWORD | admin_password | Admin account password | *Not set* |
| INVENTREE_ADMIN_EMAIL | admin_email |Admin account email address | *Not set* |

!!! info "Administrator Account"
    Providing `INVENTREE_ADMIN` credentials will result in the provided account being created with *superuser* permissions when InvenTree is started.

## Secret Key

InvenTree requires a secret key for providing cryptographic signing - this should be a secret (and unpredictable) value.

The secret key can be provided in multiple ways, with the following (descending) priorities:

**Pass Secret Key via Environment Variable**

A secret key string can be passed directly using the environment variable `INVENTREE_SECRET_KEY`

**Pass Secret Key File via Environment Variable**

A file containing the secret key can be passed via the environment variable `INVENTREE_SECRET_KEY_FILE`

**Fallback to Default Secret Key File**

If not specified via environment variables, the fallback secret_key file (automatically generated as part of InvenTree installation) will be used.

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_SECRET_KEY | secret_key | Raw secret key value | *Not set* |
| INVENTREE_SECRET_KEY_FILE | secret_key_file | File containing secret key value | *Not set* |

## Database Options

InvenTree provides support for multiple database backends - any backend supported natively by Django can be used. 

Database options are specified under the *database* heading in the configuration file. Any option available in the Django documentation can be used here - it is passed through transparently to the management scripts.

The following database options can be configured:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DB_ENGINE | database.ENGINE | Database backend | *Not set* |
| INVENTREE_DB_NAME | database.NAME | Database name | *Not set* |
| INVENTREE_DB_USER | database.USER | Database username (if required) | *Not set* |
| INVENTREE_DB_PASSWORD | database.PASSWORD | Database password (if required) | *Not set* |
| INVENTREE_DB_HOST | database.HOST | Database host address (if required) | *Not set* |
| INVENTREE_DB_PORT | database.PORT | Database host port (if required) | *Not set* |

### PostgreSQL Settings

If running with a PostgreSQL database backend, the following additional options are available:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DB_TIMEOUT | database.timeout | Database connection timeout (s) | 2 |
| INVENTREE_DB_TCP_KEEPALIVES | database.tcp_keepalives | TCP keepalive | 1 |
| INVENTREE_DB_TCP_KEEPALIVES_IDLE | database.tcp_keepalives_idle | Idle TCP keepalive | 1 |
| INVENTREE_DB_TCP_KEEPALIVES_INTERNAL | database.tcp_keepalives_internal | Internal TCP keepalive | 1|
| INVENTREE_DB_TCP_KEEPALIVES_COUNT | database.tcp_keepalives_count | TCP keepalive count | 5 |
| INVENTREE_DB_ISOLATION_SERIALIZABLE | database.serializable | Database isolation level configured to "serializable" | False |

### MySQL Settings

If running with a MySQL database backend, the following additional options are available:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_DB_ISOLATION_SERIALIZABLE | database.serializable | Database isolation level configured to "serializable" | False |

## Email Settings

To enable [email functionality](../settings/email.md), email settings must be configured here, either via environment variables or within the configuration file.

The following email settings are available:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_EMAIL_BACKEND | email.backend | Email backend module | django.core.mail.backends.smtp.EmailBackend |
| INVENTREE_EMAIL_HOST | email.host | Email server host | *Not set* |
| INVENTREE_EMAIL_PORT | email.port | Email server port | 25 |
| INVENTREE_EMAIL_USERNAME | email.username | Email account username | *Not set* |
| INVENTREE_EMAIL_PASSWORD | email.password | Email account password | *Not set* |
| INVENTREE_EMAIL_TLS | email.tls | Enable TLS support | False |
| INVENTREE_EMAIL_SSL | email.ssl | Enable SSL support | False |
| INVENTREE_EMAIL_SENDER | email.sender | Name of sender | *Not set* |
| INVENTREE_EMAIL_PREFIX | email.prefix | Prefix for subject text | [InvenTree] |

## Supported Currencies

The currencies supported by InvenTree must be specified in the [configuration file](#configuration-file).

A list of currency codes (e.g. *AUD*, *CAD*, *JPY*, *USD*) can be specified using the `currencies` variable.

## Allowed Hosts / CORS

By default, all hosts are allowed, and CORS requests are enabled from any origin.

!!! danger "Not Secure"
    Allowing access from any host is not secure, and should be adjusted for your installation.

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| *N/A* | allowed_hosts | List of allowed hosts | `*` |
| *N/A* | cors.allow_all | Allow all remote URLS for CORS checks | False |
| *N/A* | cors.whitelist | List of whitelisted CORS URLs | *Empty list* |

!!! info "Configuration File"
    Allowed hosts and CORS options must be changed in the configuration file, and cannot be set via environment variables

For further information, refer to the following documentation:

* [Django ALLOWED_HOSTS](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts)
* [Django CORS headers](https://github.com/OttoYiu/django-cors-headers)

## File Storage Locations

### Static File Storage

Static files **require** a local directory for storage. This directory should be specified with the `static_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_STATIC_ROOT` environment variable.

### Uploaded File Storage

Uploaded media files **require** a local directory for storage. This directory should be specified with the `media_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_MEDIA_ROOT` environment variable.

### Backup File Storage

Database and media backups **require** a local directory for storage. This directory should be specified with the `backup_dir` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_BACKUP_DIR` environment variable.

## Authentication

InvenTree provides allowance for additional sign-in options. The following options are not enabled by default, and care must be taken by the system administrator when configuring these settings.

### Single Sign On

SSO backends for all required authentication providers need to be added to the config file as a list under the key `social_backends`. The correct backend-name can be found in django-allauths [configuration documentation](https://django-allauth.readthedocs.io/en/latest/installation.html#django).

If the selected providers need additional settings they must be added as dicts under the key `social_providers`. The correct settings can be found in the django-allauths [provider documentation](https://django-allauth.readthedocs.io/en/latest/providers.html).

!!! warning "You are not done"
    SSO still needs credentials for all providers and has to be enabled in the [global settings](../settings/global.md)!

!!! tip "More Info"
    Refer to the [SSO documentation](../settings/SSO.md) for more information.

### Login Options

The login-experience can be altered with the following settings:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_LOGIN_CONFIRM_DAYS | login.confirm_days | Duration for which confirmation links are valid | 3 |
| INVENTREE_LOGIN_ATTEMPTS | login.attempts | Count of allowed login attempts before blocking user | 5 |

### Authentication Backends

Custom authentication backends can be used by specifying them here. These can for example be used to add [LDAP / AD login](https://django-auth-ldap.readthedocs.io/en/latest/) to InvenTree

### Sentry Integration

The InvenTree server can be integrated with the [sentry.io](https://sentry.io) monitoring service, for error logging and performance tracking.

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_SENTRY_ENABLED | sentry_enabled | Enable sentry.io integration | False |
| INVENTREE_SENTRY_DSN | sentry_dsn | Sentry DSN (data source name) key | *Defaults to InvenTree developer key* |
| INVENTREE_SENTRY_SAMPLE_RATE | sentry_sample_rate | How often to send data samples | 0.1 |

!!! info "Default DSN"
    If enabled with the default DSN, server errors will be logged to a sentry.io account monitored by the InvenTree developers.

### Customisation Options

The logo and custom messages can be changed/set:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_CUSTOM_LOGO | customize.logo | Path to custom logo in the static files directory | *Not set* |
| INVENTREE_CUSTOM_SPLASH | customize.splash | Path to custom splash screen in the static files directory | *Not set* |
| INVENTREE_CUSTOMIZE | customize.login_message | Custom message for login page | *Not set* |
| INVENTREE_CUSTOMIZE | customize.navbar_message | Custom message for navbar | *Not set* |

If you want to remove the InvenTree branding as far as possible from your end-user also check the [global server settings](../settings/global.md#server-settings). 

!!! info "Custom Splash Screen Path"
    The provided *custom splash screen* path must be specified *relative* to the location of the `/static/` directory.

!!! info "Custom Logo Path"
    The provided *custom logo* path must be specified *relative* to the location of the `/static/` directory.

## Plugin Options

The following [plugin](../extend/plugins.md) configuration options are available:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_PLUGINS_ENABLED | plugins_enabled | Enable plugin support | False |
| INVENTREE_PLUGIN_FILE | plugins_plugin_file | Location of plugin installation file | *Not set* |
| INVENTREE_PLUGIN_DIR | plugins_plugin_dir | Location of external plugin directory | *Not set* |

## Other Options

### Middleware

Custom middleware layers can specified here.