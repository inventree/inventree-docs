---
title: Database Configuration
---

## Database Configuration

Admin users will need to adjust the InvenTree installation to meet the particular needs of their setup. For example, pointing to the correct database backend, or specifying a list of allowed hosts.

The Django configuration parameters are found in the normal place (*settings.py*). However the settings presented in this file should not be adjusted as they will alter the core behaviour of the InvenTree application.

### Configuration File

To support install specific settings, a simple configuration file ``config.yaml`` is provided. This configuration file is loaded by the InvenTree server at runtime. Settings specific to a given install should be adjusted in ``config.yaml``.

!!! info "Config file location"
    The InvenTree config file is located at `./InvenTree/config.yaml`

The default configuration file launches a *DEBUG* configuration with a simple SQLITE database backend. This default configuration file is shown below:

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

### Basic Options

The following basic options are available:

| Environment Variable | Settings File | Description |
| --- | --- | --- |
| INVENTREE_DEBUG | debug | Enable debug mode |
| INVENTREE_LOG_LEVEL | log_level | Set level of logging to terminal |

### Secret Key

InvenTree requires a secret key for providing cryptographic signing - this should be a secret (and unpredictable) value.

The secret key can be provided in multiple ways, with the following (descending) priorities:

**Pass Secret Key via Environment Variable**

A secret key string can be passed directly using the environment variable `INVENTREE_SECRET_KEY`

**Pass Secret Key File via Environment Variable**

A file containing the secret key can be passed via the environment variable `INVENTREE_SECRET_KEY_FILE`

**Fallback to Default Secret Key File**

If not specified via environment variables, the fallback secret_key file (automatically generated as part of InvenTree installation) will be used.

### Database Options

InvenTree provides support for multiple database backends - any backend supported natively by Django can be used. 

Database options are specified under the *database* heading in the configuration file. Any option available in the Django documentation can be used here - it is passed through transparently to the management scripts.

The following database options can be configured:

| Environment Variable | COnfig File | Description |
| --- | --- | --- |
| INVENTREE_DB_ENGINE | database.ENGINE | Database backend |
| INVENTREE_DB_NAME | database.NAME | Database name |
| INVENTREE_DB_USER | database.USER | Database username (if required) |
| INVENTREE_DB_PASSWORD | database.PASSWORD | Database password (if required) |
| INVENTREE_DB_HOST | database.HOST | Database host address (if required) |
| INVENTREE_DB_PORT | database.PORT | Database host port (if required) |

Instructions for particular database backends are provided below:

#### SQLite
By default, InvenTree uses an sqlite database file : `inventree_db.sqlite3`. This provides a simple, portable database file that is easy to use for debug and testing purposes. 

#### MySQL
MySQL database backend is supported with the native Django implemetation. To run InvenTree with the MySQL backend, a number of extra packages need to be installed:

* mysql-server - *MySQL backend server*
* libmysqlclient-dev - *Required for connecting to the MySQL database in Python*
* (pip) mysqlclient - *Python package for communication with MySQL database*

To install these required packages, run the following command:

```
inv mysql
```

It is then up to the database adminstrator to create a new MySQL database to store inventree data, in addition to a username/password to access the data.

!!! info "MySQL Collation"
    When creating the MySQL database, the adminstrator must ensure that the collation option is set to **utf8_unicode_520_ci** to ensure that InvenTree features function correctly.

The database options (in the `config.yaml` file) then need to be adjusted to communicate the MySQL backend. Refer to the [Django docs](https://docs.djangoproject.com/en/dev/ref/databases/) for further information.

#### PostgreSQL
PostgreSQL database backend is supported with the native Django implementation. Note that to use this backend, the following system packages must be installed:

* postgresql
* postgresql-contrib
* libpq-dev
* (pip3) psycopg2

To install these required packages, run the following commands:

```
inv postgresql
```

It is then up to the database adminstrator to create a new PostgreSQL database to store inventree data, in addition to a username/password to access the data.

The database options (in the `config.yaml` file) then need to be adjusted to communicate the PostgreSQL backend. Refer to the [Django docs](https://docs.djangoproject.com/en/dev/ref/databases/) for further information.

### Email Backend

InvenTree email settings must be correctly configured to allow sending emails.

Email options are specified under the *email* heading in the configuration file. Alternatively email settings can be set via environment variables.

The following email options can be configured:

| Environment Variable | Config File | Description |
| --- | --- | --- |
| INVENTREE_EMAIL_HOST | email.host | Email service host address |
| INVENTREE_EMAIL_PORT | email.port | Email service host port |
| INVENTREE_EMAIL_USERNAME | email.username | Account username |
| INVENTREE_EMAIL_PASSWORD | email.password | Account password |
| INVENTREE_EMAIL_PREFIX | email.prefix | Email subject prefix - default is "[InvenTree] " |
| INVENTREE_EMAIL_TLS | email.tls | Enable TLS support |
| INVENTREE_EMAIL_SSL | email.ssl | Enable SSL support |

### Allowed Hosts / CORS

By default, all hosts are allowed, and CORS requests are enabled from any origin. **This is not secure and should be adjusted for your installation**. These options can be changed in the configuration file.

For further information, refer to the following documentation:

* [Django ALLOWED_HOSTS](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts)
* [Django CORS headers](https://github.com/OttoYiu/django-cors-headers)

### Static File Storage

By default, static files are stored in the local directory `./inventree_media`. This directory should be changed by specifying the `static_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_STATIC_ROOT` environment variable.

### Uploaded File Storage

By default, uploaded media files are stored in the local directory `./inventree_media`. This directory should be changed by specifying the `media_root` option in the config file based on the particular installation requirements.

Alternatively this location can be specified with the `INVENTREE_MEDIA_ROOT` environment variable.

### Backup Location

The default behaviour of the database backup is to generate backup files for database tables and media files to the user's temporary directory. The target directory can be overridden by setting the `backup_dir` parameter in the config file.

Alternatively this location can be specified with the `INVENTREE_BACKUP_DIR` environment variable.

### Authentication Backends

Custom authentication backends can be used by specifying them here

### Middleware

Custom middleware layers can specified here.