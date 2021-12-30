---
title: Plugins
---

## InvenTree Plugin Architecture

The InvenTree server code supports an extensible plugin architecture, allowing custom plugins to be integrated directly into the database server. This allows development of complex behaviours which are decoupled from core InvenTree code.

InvenTree built-in plugins are located in the directory `./InvenTree/plugin/builtin`.  
Custom plugins should be placed  in the directory `./InvenTree/plugins`.

Plugins are discovered and loaded when the server is started.

Multiple plugins are supported:

* [Reporting plugins](./plugins/report.md)
* [Barcode plugins](./plugins/barcode.md)
* [Action plugins](./plugins/action.md)
* [Integration plugins](./plugins/integration.md)
