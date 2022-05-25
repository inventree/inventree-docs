---
title: Plugins
---

## InvenTree Plugin Architecture

The InvenTree server code supports an extensible plugin architecture, allowing custom plugins to be integrated directly into the database server. This allows development of complex behaviours which are decoupled from core InvenTree code.

Plugins can be added from multiple sources:

- Plugins can be installed via PIP (python package manager)
- Custom plugins should be placed in the directory `./InvenTree/plugins`.
- InvenTree built-in plugins are located in the directory `./InvenTree/plugin/builtin`.  

Note: Plugins are discovered and loaded only when the server is started.

!!! info "Enable Plugin Support"
    To enable custom plugins, plugin support must be activated in the [server configuration](../start/config.md).

!!! question "Have you tried turning it off and on again?"
    When new plugins are installed (and activated), both the web server and background worker must be restarted.

### Plugin Base Class

Custom plugins must inherit from the [InvenTreePlugin class](https://github.com/inventree/InvenTree/blob/2d1776a151721d65d0ae007049d358085b2fcfd5/InvenTree/plugin/plugin.py#L204). Any plugins installed via the methods outlined above will be "discovered" when the InvenTree server launches.

!!! warning "Namechange"
    The name of the base class was changed with `0.7.0` from `IntegrationPluginBase` to `InvenTreePlugin`. While the old name is still available till `0.8.0` we strongly suggest upgrading your plugins. Deprecation warnings are raised if the old name is used.

### Imports

As the code base is evolving import paths might change. Therefore we provide stable import targets for important python APIs.  
Please read all release notes and watch out for warnings - we generally provide backports for depreciated interfaces for at least one minor release.

#### Plugins

Generall classes an mechanisms are provided under the `plugin` [namespaces](https://github.com/inventree/InvenTree/blob/master/InvenTree/plugin/__init__.py). These include:

```python
# Management objects
registry                    # Object that manages all plugin states and integrations

# Base classes
InvenTreePlugin             # Base class for all plugins

# Errors
MixinImplementationError    # Is raised if a mixin is implemented wrong (default not overwritten for example)
MixinNotImplementedError    # Is raised if a mixin was not implemented (core mechanisms are missing from the plugin)
```

#### Mixins

Mixins are split up internally to keep the source tree clean and enable better testing seperation. All public APIs that should be used are exposed under `plugin.mixins`. These include all built-in mixins and notification methods. An up-to-date reference can be found in the source code (current master can be [found here](https://github.com/inventree/InvenTree/blob/master/InvenTree/plugin/mixins/__init__.py)).

#### Models and other internal InvenTree APIs

!!! warning "Danger Zone"
    The APIs outside of the `plugin` namespace are not structured for public usage and require a more in-depth knowledge of the Django framework. Please ask in GitHub discussions of the `ÌnvenTree` org if you are not sure you are using something the intended way.

We do not provide stable interfaces to models or any other internal python APIs. If you need to integrate into these parts please make yourself familiar with the codebase. We follow general Django patterns and only stray from them in limited, special cases.  
If you need to react to state changes please use the [EventMixin](./plugins/event.md).

### Plugin Options

Some metadata options can be defined as constants in the plugins class.

``` python
NAME = '' # Used as a general reference to the plugin
SLUG = None  # Used in URLs, setting-names etc. when a unique slug as a reference is needed -> the plugin name is used if not set
TITLE = None  # A nice human friendly name for the plugin -> used in titles, as plugin name etc.

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
    Newly discovered plugins are disabled by default, and must be manually enabled (in the admin interface) by a user with staff privileges.

### Plugin Mixins

Common use cases are covered by pre-supplied modules in the form of *mixins* (similar to how [django](https://docs.djangoproject.com/en/stable/topics/class-based-views/mixins/) does it). Each mixin enables the integration into a specific area of InvenTree. Sometimes it also enhances the plugin with helper functions to supply often used functions out-of-the-box.

Supported mixin classes are:

- [ActionMixin](./plugins/action.md)
- [APICallMixin](./plugins/api.md)
- [AppMixin](./plugins/app.md)
- [BarcodeMixin](./plugins/barcode.md)
- [EventMixin](./plugins/event.md)
- [LabelPrintingMixin](./plugins/label.md)
- [LocateMixin](./plugins/locate.md)
- [NavigationMixin](./plugins/navigation.md)
- [PanelMixin](./plugins/panel.md)
- [ScheduleMixin](./plugins/schedule.md)
- [SettingsMixin](./plugins/settings.md)
- [UrlsMixin](./plugins/urls.md)

## Installing a Plugin

Plugins can either be loaded from paths in the InvenTree install directory or as a plugin installed via pip. We recommend installation via pip as this enables hassle-free upgrades.

### Builtin Plugins

Built-In plugins ship in `src/InvenTree/plugin/builtin`. To achive full unit-testing for all mixins there are some sample implementations in `src/InvenTree/plugin/samples`. These are not loaded in production mode.

### Local Directory

Custom plugins can be placed in the `src/InvenTree/plugins/` directory, where they will be automatically discovered. This can be useful for developing and testing plugins, but can prove more difficult in production (e.g. when using Docker). 

### Plugin Installation File (PIP)

Plugins installation can be simplified by providing a list of plugins in a plugin configuration file. This file (by default, 'plugins.txt' in the same directory as the server configuration file) contains a list of required plugin packages.

Plugins can be then installed from this file by simply running the command `invoke plugins`.

!!! success "Auto Update"
    When the server installation is updated via the `invoke update` command, the plugins (as specified in *plugins.txt*) will also be updated automatically.

