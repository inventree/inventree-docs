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

### Command 'inv' / 'invoke' not found

If the `inv` or `invoke` command does not work, it means that the [invoke](https://pypi.org/project/invoke/) python library has not been correctly installed. 

Update the installed python packages with PIP:

```
pip3 install -U -r requirements.txt
```

### ModuleNotFoundError: No module named 'django'

Most likely you are trying to run the InvenTree server from outside the context of the virtual environment where the required python libraries are installed.

Always activate the virtual environment before running server commands!