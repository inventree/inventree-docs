---
title: Background Tasks
---

## Background Tasks

In addition to managing the database and providing a web interface, InvenTree runs various background tasks;

### Blocking Operations

Some tasks (such as sending emails or performing bulk database actions) may take a significant amount of time. Instead of delaying the response to the user, these tasks are handled by the background task manager.

### Periodic Tasks

Some tasks must be performed on a periodic basis. 

## Django Q 

InvenTree uses the [django-q](https://django-q.readthedocs.io/en/latest/) background task manager.

## Admin Interface

Scheduled tasks can be viewed in the InvenTree admin interface.
