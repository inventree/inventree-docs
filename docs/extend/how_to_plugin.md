---
title: How to plugin
---

## How to write a plugin
A short introductory guide for plugin beginners.

### Should it be a plugin?
First of all figure out what you function / code should do.
If you want to change how InvenTree base mechanics and business logic work a plugin will not be sufficient. Maybe fork the project or better start a discussion on GitHub.

If you want to remove parts of the user interface -> remove the permissions for that part and the users will not see them.

If you add a lot of code (over ~1000 LOC) maybe spilt it into multiple plugins to make upgrading specific parts and testing simpler.

### It will be a plugin! Now pick your mixins
Great. Now please read the plugin documentation to figure out the basic way it works. It is rather short as a the (builtin) mixins come with extensive docstrings.

Consider the usecase for your plugin and define the exact function of the plugin, maybe even in a short readme. The pick the mixins you need. They help reduce custom code and keep the system reliable if internal calls change.

- Is it just a simple REST-endpoint that runs a function (ActionMixin) or a parser for a custom barcode format (BarcodeMixin)?
- How does the user interact with the plugin? Is it a UI separate from the main InvenTree UI (UrlsMixin), does it need multiple pages with navigation-links (NavigationMixin).
- Will it make calls to external APIs (APICallMixin helps there)?
- Do you need to run in the background (ScheduleMixin) or when things in InvenTree change (EventMixin)?
- Does the plugin need configuration that should be user changeable (SettingsMixin) or static (just use a yaml in the config dir)?
- You want to receive webhooks? Do not code your own untested function – use the WebhookEndpoint model as a base and override the perform_action method.
- Do you need the full power of Django with custom models and all the complexity that comes with that – welcome to the danger zone and AppMixin.
