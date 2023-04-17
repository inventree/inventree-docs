---
title: Purchase Order Report
---

## Purchase Order Reports

Custom purchase order reports may be generated against any given [Purchase Order](../buy/po.md). For example, purchase order reports could be used to generate a pdf of the order to send to a supplier.

### Purchase Order Filters

The report template can be filtered against available [Purchase Order](../buy/po.md) instances.

### Context Variables

In addition to the default report context variables, the following variables are made available to the purchase order report template for rendering:

| Variable | Description |
| --- | --- |
| order | The specific Purchase Order object |
| reference | The order reference field (can also be accessed as `{% raw %}{{ order.description }}{% endraw %}`) |
| description | The order description field |
| supplier | The [supplier](../buy/supplier.md) associated with this purchase order |
| lines | A list of available line items for this order |
| extra_lines | A list of available *extra* line items for this order | 

### Default Report Template

A default *Purchase Order Report* template is provided out of the box, which is useful for generating simple test reports. Furthermore, it may be used as a starting point for developing custom BOM reports:

View the [source code](https://github.com/inventree/InvenTree/blob/master/InvenTree/report/templates/report/inventree_po_report_base.html) for the default purchase order report template.
