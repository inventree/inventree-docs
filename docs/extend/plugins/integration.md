---
title: Integration Plugins
---

### Integration Plugins

Integration Plugins provide a wide area of deep integration into the interface of InvenTree.

For an example of a pretty much full Integration Plugin, refer to `/InvenTree/plugin/samples/integration/sample.py`

#### Plugin Options

Some metadata options can be defined as constants in the plugins class.

``` python
PLUGIN_SLUG = None  # Used in URLs, setting-names etc. when a unique slug as a reference is needed -> the plugin name is used if not set
PLUGIN_TITLE = None  # A nice human friendly name for the plugin -> used in titles, as plugin name etc.

AUTHOR = None  # Author of the plugin, git commit information is used if not present
PUBLISH_DATE = None  # Publishing date of the plugin, git commit information is used if not present
VERSION = None  # Version of the plugin
WEBSITE = None  # Website for the plugin, developer etc. -> is shown in plugin overview if set
```



#### Installing a Plugin

Plugins can either be loaded from paths in the InvenTree install directory or as a plugin installed via pip. We recommend installation via pip as this enables hassle-free upgrades.

For development new plugins can be placed ina a subdirectroy in `src/InvenTree/plugins`. Built-In plugins ship in `src/InvenTree/plugin/builtin`. To achive full unit-testing for all mixins there are some sample implementations in `src/InvenTree/plugin/samples`. These are not loaded in production mode.

#### Mixins

Common use cases are covered by pre-supplied modules in the form of mixins (similar to how [django](https://docs.djangoproject.com/en/stable/topics/class-based-views/mixins/) does it). Each mixin enables the integration into a specific area of InvenTree. Sometimes it also enhances the plugin with helper functions to supply often used functions out-of-the-box.

##### Basic Mixin Functions

All mixins are registered with the plugin on start-up so you can access all added mixins as a dict with the `plugin.registered_mixins` property that is added to each plugin.

The function `plugin.mixin_enabled(key)` returns if a mixin is present in a plugin and configured correctly.

##### Initialisation

Each mixin must call `super().__init__()` in it's `__init__` function and register itself with a call to `self.add_mixin()`. Check out the built-in mixins for examples.

``` python
def __init__(self):
    super().__init__()
    self.add_mixin('settings', 'has_settings', __class__)
```

##### Meta Options

Each mixin can define additional options as a Meta subclass. These are used to describe the mixin.


#### SettingsMixin

Use the class constant `SETTINGS` for a dict of settings that should be added as global database settings.  
The dict must be formatted similar to the following sample. Take a look at the settings defined in `InvenTree.common.models.InvenTreeSetting` for all possible parameters.


``` python
SETTINGS = {
    'PO_FUNCTION_ENABLE': {
        'name': _('Enable PO'),
        'description': _('Enable PO functionality in InvenTree interface'),
        'default': True,
        'validator': bool,
    },
}
```

!!! note "Use carefully"
    All global and user settings are exposed to the frontend code and can be read out via the browsers developer tools. You can protect a setting from export by adding `'protected': True` to sensitive settings.
    You can access settings in frontend JS code under the global variable `global_settings`.

This mixin defines the helper functions `plugin.get_setting` and `plugin.set_seting` to access all plugin specific settings.


#### UrlsMixin

Use the class constant `URLS` for a array of URLs that should be added to InvenTrees URL paths or override the `plugin.setup_urls` function.  
The array has to contain valid URL patterns as defined in the [django documentation](https://docs.djangoproject.com/en/stable/topics/http/urls/).

``` python
URLS = [
    url(r'increase/(?P<location>\d+)/(?P<pk>\d+)/', self.view_increase, name='increase-level'),
]
```

The URLs get exposed under `/plugin/{plugin.slug}/*` and get exposed to the template engine with the prefix `plugin:{plugin.slug}:` (for usage with the [url tag](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#url)).


#### NavigationMixin

Use the class constant `NAVIGATION` for a array of links that should be added to InvenTrees navigation header.  
The array must contain at least one dict that at least define a name and a link for each element. The link must be formatted for a URL pattern name lookup - links to external sites are not possible directly. The optional icon must be a class reference to an icon (InvenTree ships with fontawesome 4 by default).

``` python
NAVIGATION = [
    {'name': 'SampleIntegration', 'link': 'plugin:sample:hi', 'icon': 'fas fa-box'},
]
```

The optional class constants `NAVIGATION_TAB_NAME` and `NAVIGATION_TAB_ICON` can be used to change the name and icon for the parent navigation node.


#### AppMixin

If this mixin is added to a plugin the directory the plugin class is defined in is added to InvenTrees `INSTALLED_APPS`.

!!! warning "Danger Zone"
    Only use this plugin if you have an understanding of djangos [app system](https://docs.djangoproject.com/en/stable/ref/applications). Plugins with this mixin are deeply integrated into InvenTree and can cause difficult to reproduce or long-running errors. Use the built-in testing functions of django to make sure your code does not cause unwanted behaviour in InvenTree.
