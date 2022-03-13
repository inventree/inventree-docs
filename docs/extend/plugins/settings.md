---
title: Settings Mixin
---

## SettingsMixin

The *SettingsMixin* allows the plugin to save and load persistent settings to the database.

- Plugin settings are stored against the individual plugin, and thus do not have to be unique
- Plugin settings are stored using a "key:value" pair

Use the class constant `SETTINGS` for a dict of settings that should be added as global database settings.  

The dict must be formatted similar to the following sample. Take a look at the settings defined in `InvenTree.common.models.InvenTreeSetting` for all possible parameters.


``` python
class PluginWithSettings(SettingsMixin, IntegrationPluginBase):
    
    PLUGIN_NAME = "PluginWithSettings"
    
    SETTINGS = {
        'API_ENABLE': {
            'name': 'API Functionality',
            'description': 'Enable remote API queries',
            'validator': bool,
            'default': True,
        },
        'API_KEY': {
            'name': 'API Key',
            'description': 'Security key for accessing remote API',
            'default': '',
        },
        'API_URL': {
            'name': _('API URL'),
            'description': _('Base URL for remote server'),
            'default': 'http://remote.url/api',
        },
    }
```

This mixin defines the helper functions `plugin.get_setting` and `plugin.set_seting` to access all plugin specific settings:

```python
api_url = self.get_setting('API_URL')
```


