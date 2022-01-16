---
title: How to plugin
---

## How to write a plugin
A short introductory guide for plugin beginners.

### Should it be a plugin?
First of all figure out what your plugin / code should do.
If you want to change how InvenTree base mechanics and business logic work, a plugin will not be sufficient. Maybe fork the project or better [start a discussion](https://github.com/inventree/InvenTree/discussions) on GitHub. There might be an easier / established way to do what you want.

If you want to remove parts of the user interface -> remove the permissions for those objects / actions and the users will not see them.

If you add a lot of code (over ~1000 LOC) maybe split it into multiple plugins to make upgrading and testing simpler.

### It will be a plugin!
Great. Now please read the [plugin documentation](./plugins.md) to get an overview of the architecture. It is rather short as a the (builtin) mixins come with extensive docstrings.

### Pick your building blocks
Consider the usecase for your plugin and define the exact function of the plugin, maybe wrtie it down in a short readme. Then pick the mixins you need (they help reduce custom code and keep the system reliable if internal calls change).

- Is it just a simple REST-endpoint that runs a function ([ActionMixin](./plugins/action.md)) or a parser for a custom barcode format ([BarcodeMixin](./plugins/barcode.md))?
- How does the user interact with the plugin? Is it a UI separate from the main InvenTree UI ([UrlsMixin](./plugins/urls.md)), does it need multiple pages with navigation-links ([NavigationMixin](./plugins/navigation.md)).
- Will it make calls to external APIs ([APICallMixin](./plugins/api.md) helps there)?
- Do you need to run in the background ([ScheduleMixin](./plugins/schedule.md)) or when things in InvenTree change ([EventMixin](./plugins/event.md))?
- Does the plugin need configuration that should be user changeable ([SettingsMixin](./plugins/settings.md)) or static (just use a yaml in the config dir)?
- You want to receive webhooks? Do not code your own untested function, use the WebhookEndpoint model as a base and override the perform_action method.
- Do you need the full power of Django with custom models and all the complexity that comes with that – welcome to the danger zone and [AppMixin](./plugins/app.md). The plugin will be treated as a app by django and can maybe rack the whole instance.
