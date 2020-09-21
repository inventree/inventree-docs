---
title: Plugins
layout: page
---

## InvenTree Plugin Architecture

The InvenTree server code supports an extensible plugin architecture, allowing custom plugins to be integrated directly into the database server. This allows development of complex behaviours which are decoupled from core InvenTree code.

InvenTree plugins are located in the directory `./InvenTree/plugins/`.

Plugins are discovered and loaded when the server is started.

Multiple plugins are supported:

### Reporting Plugins

InvenTree can generate customized reports (for example stocktake information, packing lists, acceptance test reports, etc). The reporting interface is extremely versatile, allowing the generation of reports in multiple formats (PDF / LaTeX / etc).

!!! missing "TODO"
	Include more information here on reporting plugins

### Barcode Plugins

InvenTree supports decoding of arbitrary barcode data via a **Barcode Plugin** interface. Barcode data POSTed to the `/api/barcode/` endpoint will be supplied to all loaded barcode plugins, and the first plugin to successfully interpret the barcode data will return a response to the client.

InvenTree can generate native QR codes to represent database objects (e.g. a single StockItem). This barcode can then be used to perform quick lookup of a stock item or location in the database. A client application (for example the InvenTree mobile app) scans a barcode, and sends the barcode data to the InvenTree server. The server then uses the **InvenTreeBarcodePlugin** (found at `/InvenTree/plugins/barcode/inventree.py`) to decode the supplied barcode data.

Any third-party barcodes can be decoded by writing a matching plugin to decode the barcode data. These plugins could then perform a server-side action, or render a JSON response back to the client for further action.

Some examples of possible uses for barcode integration:

- Stock lookup by scanning a barcode on a box of items
- Receiving goods against a PurchaseOrder by scanning a supplier barcode
- Perform a stock adjustment action (e.g. take 10 parts from stock whenever a barcode is scanned)

Barcode data are POSTed to the server as follows:

```
POST {
    barcode_data: "[(>someBarcodeDataWhichThePluginKnowsHowToDealWith"
}
```

### Action Plugins

Arbitrary "actions" can be called by POSTing data to the `/api/action/` endpoint. The POST request must include the name of the action to be performed, and a matching ActionPlugin plugin must be loaded by the server. Arbitrary data can also be provided to the action plugin via the POST data:

```
POST {
    action: "MyCustomAction",
    data: {
        foo: "bar",
    }
}
```

For an example of a very simple action plugin, refer to `/InvenTree/plugins/action/action.py`