---
title: FAQ
---

## Frequently Asked Questions

### Feature *x* is not visible after update

If a particular menu / item is not visible after updating InvenTree, it may be due to your internet browser caching old versions of CSS and JavaScript files.

Before [raising an issue](https://github.com/inventree/inventree/issues), try hard-refreshing the browser cache:

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>

or

<kbd>Ctrl</kbd> + <kbd>F5</kbd>

### Problems Installing on Windows

InvenTree installation is not officially supported natively on Windows. Install using the WSL framework.

### Command 'inv' / 'invoke' not found

If the `inv` or `invoke` command does not work, it means that the [invoke](https://pypi.org/project/invoke/) python library has not been correctly installed. 

Update the installed python packages with PIP:

```
pip3 install -U -r requirements.txt
```

### ModuleNotFoundError: No module named 'django'

Most likely you are trying to run the InvenTree server from outside the context of the virtual environment where the required python libraries are installed.

Always activate the virtual environment before running server commands!

### Background Worker "Not Running"

The background worker process must be started separately to the web-server application.

From the top-level source directory, run the following command from a separate terminal, while the server is already running:

```
invoke worker
```

!!! info "Supervisor"

A better option is to manage the background worker process using a process manager such as supervisor. Refer to the [production server guide](../start/production).
