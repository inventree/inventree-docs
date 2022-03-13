---
title: Plugins
---

## InvenTree Plugin Architecture

The InvenTree server code supports an extensible plugin architecture, allowing custom plugins to be integrated directly into the database server. This allows development of complex behaviours which are decoupled from core InvenTree code.

Plugins can be added from multiple sources:
- InvenTree built-in plugins are located in the directory `./InvenTree/plugin/builtin`.  
- Custom plugins should be placed  in the directory `./InvenTree/plugins`.
- Plugins can be installed via PIP (python package manager)

Plugins are discovered and loaded when the server is started.

!!! info "Enable Plugin Support"
    To enable custom plugins, plugin support must be activated in the [server configuration](../start/config.md).

### Plugin Base Class

Custom plugins must inherit from the [IntegrationPluginBase class](https://github.com/inventree/InvenTree/blob/master/InvenTree/plugin/integration.py). Any plugins installed via the methods outlined above will be "discovered" when the InvenTree server launches.

### Plugin Options

Some metadata options can be defined as constants in the plugins class

``` python
PLUGIN_SLUG = None  # Used in URLs, setting-names etc. when a unique slug as a reference is needed -> the plugin name is used if not set
PLUGIN_TITLE = None  # A nice human friendly name for the plugin -> used in titles, as plugin name etc.

AUTHOR = None  # Author of the plugin, git commit information is used if not present
PUBLISH_DATE = None  # Publishing date of the plugin, git commit information is used if not present
VERSION = None  # Version of the plugin
WEBSITE = None  # Website for the plugin, developer etc. -> is shown in plugin overview if set
```

Refer to the [sample plugins](https://github.com/inventree/InvenTree/tree/master/InvenTree/plugin/samples) for further examples.

### Plugin Config

A *PluginConfig* database entry will be created for each plugin "discovered" when the server launches. This configuration entry is used to determine if a particular plugin is enabled.

The configuration entries must be enabled via the [InvenTree admin interface](../settings/admin.md).

!!! warning "Disabled by Default"
    Newly discovered plugins are disabled by default, and must be manually enabled by an admin user

### Plugin Mixins

Common use cases are covered by pre-supplied modules in the form of mixins (similar to how [django](https://docs.djangoproject.com/en/stable/topics/class-based-views/mixins/) does it). Each mixin enables the integration into a specific area of InvenTree. Sometimes it also enhances the plugin with helper functions to supply often used functions out-of-the-box.

Supported mixin classes are:

- [ActionMixin](./plugins/action.md)
- [APICallMixin](./plugins/api.md)
- [AppMixin](./plugins/app.md)
- [BarcodeMixin](./plugins/barcode.md)
- [EventMixin](./plugins/event.md)
- [NavigationMixin](./plugins/navigation.md)
- [ScheduleMixin](./plugins/schedule.md)
- [SettingsMixin](./plugins/settings.md)
- [UrlsMixin](./plugins/urls.md)

## Installing a Plugin

Plugins can either be loaded from paths in the InvenTree install directory or as a plugin installed via pip. We recommend installation via pip as this enables hassle-free upgrades.

For development new plugins can be placed ina a subdirectory in `src/InvenTree/plugins`. Built-In plugins ship in `src/InvenTree/plugin/builtin`. To achive full unit-testing for all mixins there are some sample implementations in `src/InvenTree/plugin/samples`. These are not loaded in production mode.

### Plugin Installation File

Plugins installation can be simplified by providing a list of plugins in a plugin configuration file. This file (by default, 'plugins.txt' in the same directory as the server configuration file) contains a list of required plugin packages.

Plugins can be installed from this file by simply running the command `invoke plugins`.
