---
title: Installing Plugins
---


## Installing a Plugin

Plugins can either be loaded from paths in the InvenTree install directory or as a plugin installed via pip. We recommend installation via pip as this enables hassle-free upgrades.

### Plugin Installation File (PIP)

Plugins installation can be simplified by providing a list of plugins in a plugin configuration file. This file (by default, *plugins.txt* in the same directory as the server configuration file) contains a list of required plugin packages.

Plugins can be then installed from this file by simply running the command `invoke plugins`.

Installation via PIP (using the *plugins.txt* file) provides a number of advantages:

- Any required secondary packages are installed automatically
- You can update plugins simply by specifying version numbers in *plugins.txt*
- Migrating plugins between systems is simplified
- You can install plugins via any source supported by PIP

!!! success "Auto Update"
    When the server installation is updated via the `invoke update` command, the plugins (as specified in *plugins.txt*) will also be updated automatically.


### Builtin Plugins

Built-In plugins ship in `src/InvenTree/plugin/builtin`. To achive full unit-testing for all mixins there are some sample implementations in `src/InvenTree/plugin/samples`.

!!! info "Debug Only"
    The sample plugins are not loaded in production mode.

### Local Directory

Custom plugins can be placed in the `src/InvenTree/plugins/` directory, where they will be automatically discovered. This can be useful for developing and testing plugins, but can prove more difficult in production (e.g. when using Docker). 

!!! info "Git Tracking"
    The `src/InvenTree/plugins/` directory is excluded from Git version tracking - any plugin files here will be hidden from Git

!!! warning "Not Recommended For Production"
    Loading plugins via the local *plugins* directory is not recommended for production. If you cannot use PIP installation (above), specify a custom plugin directory (below) or use a [VCS](https://pip.pypa.io/en/stable/topics/vcs-support/) as a plugin install source.

### Custom Directory

If you wish to install plugins from local source, rather than PIP, it is better to place your plugins in a directory outside the InvenTree source directory.

To achieve this, set the `INVENTREE_PLUGIN_DIR` environment variable to the directory where locally sourced plugins are located. Refer to the [configuration options](../../start/config.md#plugin-options) for further information.

!!! info "Docker"
    When running InvenTree in docker, a *plugins* directory is automatically created in the mounted data volume. Any plugins can be placed there, and will be automatically loaded when the server is started.
