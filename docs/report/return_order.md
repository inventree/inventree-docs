---
title: Return Order Reports
---

## Return Order Reports

Custom reports may be generated against any given [Return Order](../sell/return.md). For example, return order reports can be used to generate an RMA request to send to a customer.

### Context Variables

In addition to the default report context variables, the following context variables are made available to the return order report template for rendering:

| Variable | Description |
| --- | --- |
| order | The return order object the report is being generated against |
| description | The description of the order, also accessed through `order.description` |
| reference | The reference of the order, also accessed through `order.reference` |
| customer | The customer object related to this order |
| lines | The list of line items linked to this order |
| extra_lines | The list of extra line items linked to this order |

### Default Report

A default report template is provided out of the box, which can be used as a starting point for developing custom return order report templates.

!!! tip "Take a Peek"
    View the [source code](https://github.com/inventree/InvenTree/blob/master/InvenTree/report/templates/report/inventree_return_order_report_base.html) to peer under the hood!
