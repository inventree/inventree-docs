---
title: Installation Instructions
---

## Development Server

The following installation instructions can be used to install InvenTree and run a server which provides a simple development environment.

!!! warning "Deployment"
    Refer to the [deployment instructions](../deploy) to implement a much more robust server setup.

## Download Code



InvenTree setup is performed using the [invoke](https://www.pyinvoke.org/) Python build tool. Various useful scripts are defined in the `tasks.py` file.

Install invoke as follows:

```
pip3 install invoke
```

!!! warning "Invoke Version"
	InvenTree requires invoke version 1.4.0 or newer. Some platforms may be shipped with older versions of invoke!

To display a list of the available configuration scripts, run the following command:

```
inv --list
```

### Database Configuration

Once the required packages are installed, the database configuration must be adjusted to suit your particular needs. InvenTree provides a simple default setup which should work *out of the box* for testing and debug purposes.

As part of the previous *install* step, a configuration file (**config.yaml**) is created. The configuration file provides administrators control over various setup options without digging into the Django *settings.py* script. The default setup uses a local sqlite database with *DEBUG* mode enabled.

### Initialize Database

Once install settings are correctly configured (in *config.yaml*) run the initial setup script:

```
inv migrate
```

This performs the initial database migrations, creating the required tables, etc.

The database should now be installed!

### Create Admin Account

Create an initial superuser (administrator) account for the InvenTree instance:

```
inv superuser
```

!!! warning "Solving Cairo Errors"
	In the case the above command returns errors with the `Cairo` package, it implies that dependencies for the `weasyprint` package are not installed on the system. To solve them, run through the [weasyprint installation steps](https://weasyprint.readthedocs.io/en/stable/install.html) then re-run `inv install` and `inv superuser`.

### Run Development Server

The InvenTree database is now setup and ready to run. A simple development server can be launched from the command line. 

To launch the development server, run the following commands:

```
inv server
```

For more server options, run:

```
inv server -h
```

This will launch the InvenTree web interface at `http://127.0.0.1:8000`. For other options refer to the [django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/)

### Run Production Server

For a production install, refer to [deployment instructions](../deploy).
