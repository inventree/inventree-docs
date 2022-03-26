---
title: Label Mixin
---

## LabelPrintingMixin

The `LabelPrintingMixin` class enables plugins to print labels directly to a connected printer.

An example of this is the [inventree-brother-plugin](https://github.com/inventree/inventree-brother-plugin) which provides native support for the Brother QL and PT series of networked label printers.

If label printing plugins are enabled, they are able to be used directly from the InvenTree web interface:

{% with id="label_print", url="plugin/print_label_select_plugin.png", description="Print label via plugin" %}
{% include 'img.html' %}
{% endwith %}