---
title: Production Server
---

## Production Server

!!! warning "Installation"
    Before continuing, ensure that the [installation steps](../install) have been completed.

The following instructions provide a reasonably performant server, using [gunicorn](https://gunicorn.org/) as a webserver, and [supervisor](http://supervisord.org/) as a process manager.

For alternative deployment methods, django apps provide multiple deployment methods - see the [Django documentation](https://docs.djangoproject.com/en/2.2/howto/deployment/).

There are also numerous online tutorials describing how to deploy a Django application either locally or on an online platform.

### Gunicorn

The InvenTree web server is hosted using [Gunicorn](https://gunicorn.org/). Gunicorn is a Python WSGI server which provides a multi-worker server which is well suited to handling multiple simultaneous requests. Gunicorn is a solid choice for a production server which is easy to configure and performs well in a multi-user environment.

### Supervisor

[Supervisor](http://supervisord.org/) is a process control system which monitors and controls multiple background processes. It is used in the InvenTree production setup to ensure that the server and background worker processes are always running.

## Setup

## Start Supervisor