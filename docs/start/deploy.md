---
title: Deploy InvenTree
layout: page
---

## Deploying InvenTree

The development server provided by the Django ecosystem may be fine for a testing environment or small contained setups. However special consideration must be given when deploying InvenTree in a real-world environment.

Django apps provide multiple deployment methods - see the [Django documentation](https://docs.djangoproject.com/en/2.2/howto/deployment/).

There are also numerous online tutorials describing how to deploy a Django application either locally or on an online platform.

### Development Server

The InvenTree development server is useful for testing and configuration - and it may be wholly sufficient for a small-scale installation.

#### Running on a Local Machine

To run the development server on a local machine, run the command:

```
invoke server -a 127.0.0.1:8000
```

Serving on the address `127.0.0.1` means that InvenTree will only be available *on that computer*. The server will be accessible from a web browser on the same computer, but not from any other computers on the local network.

#### Running on a Local Network

To enable access to the InvenTree server from other computers on a local network, you need to know the IP of the computer running the server. For example, if the server IP address is `192.168.120.1`:

```
invoke server -a 192.168.120.1:8000
```

## Gunicorn

Following is a simple tutorial on serving InvenTree using [Gunicorn](https://gunicorn.org/). Gunicorn is a Python WSGI server which provides a multi-worker server which is well suited to handling multiple simultaneous requests. Gunicorn is a solid choice for a production server which is easy to configure and performs well in a multi-user environment.

### Install Gunicorn

Gunicorn can be installed using PIP:

```
pip3 install gunicorn
```

### Configure Static Directories

Directories for storing *media* files and *static* files should be specified in the ``config.yaml`` configuration file. These directories are the ``MEDIA_ROOT`` and ``STATIC_ROOT`` paths required by the Django app. Ensure that both of these directories are correctly configured for your setup.

### Collect Static Files

The required static files must be collected into the specified ``STATIC_ROOT`` directory:

```
invoke static
```

This command collects all of the required static files (including script and css files) into the specified directory ready to be served.

### Configure Gunicorn

The Gunicorn server can be configured with a simple configuration file (e.g. python script). An example configuration file is provided in ``InvenTree/gunicorn.conf.py``

``` python
{% include 'gunicorn.conf.py' %}
```

This file can be used to configure the Gunicorn server to match particular requirements.

### Run Gunicorn

```
cd InvenTree
gunicorn -c gunicorn.conf.py InvenTree.wsgi
```
