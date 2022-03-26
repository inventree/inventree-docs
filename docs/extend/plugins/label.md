---
title: Label Mixin
---

## LabelPrintingMixin

The `LabelPrintingMixin` class enables plugins to print labels directly to a connected printer. Custom plugins can be written to support any printer backend.

An example of this is the [inventree-brother-plugin](https://github.com/inventree/inventree-brother-plugin) which provides native support for the Brother QL and PT series of networked label printers.

### Web Integration

If label printing plugins are enabled, they are able to be used directly from the InvenTree web interface:

{% with id="label_print", url="plugin/print_label_select_plugin.png", description="Print label via plugin" %}
{% include 'img.html' %}
{% endwith %}

### App Integration

Label printing plugins also allow direct printing of labels via the [mobile app](../../app/stock.md#print-label)

## Implementation

Plugins which implement the `LabelPrintingMixin` mixin class must provide a `print_label` function:

```python
from dummy_printer import printer_backend

class MyLabelPrinter(LabelPrintingMixin, IntegrationPluginBase):
    """
    A simple example plugin which provides support for a dummy printer.

    A more complex plugin would communicate with an actual printer!
    """

    PLUGIN_NAME = "MyLabelPrinter"
    PLUGIN_SLUG = "mylabel"
    PLUGIN_TITLE = "A dummy printer"

    def print_label(self, label):
        """
        Send the label to the printer
        
        Arguments:
            label: A PIL (pillow) Image file
        """

        printer_backend.print(label)
```


