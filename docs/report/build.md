---
title: Build Order Report
---

## Build Order Report

Custom build order reports may be generated against any given Build Order. For example, build order reports can be used to generate work orders.

### Build Filters

!!! missing "TODO"
    This section requires further work

### Context Variables

In addition to the default report context variables, the following context variables are made available to the build order report template for rendering:

| Variable | Description |
| --- | --- |
| build | The [Build](./context_variables.md#build) object the report is being generated against |
| part | The [Part](./context_variables.md#part) object that the build references |
| reference | The build order reference string. This is just the string that follows BO... |
| title | The full name of the build including the BO |
| quantity | Build order quantity |
| build.title | The description of the build |
| build.status | The status of the build. 20 means 'Production' |
| build.bom_items | A query set with all bom items for the build |

bom_items that can be looped using {%for line in build.bom_items %} Each bom_item line has further context variables.

| Variable | Description |
| --- | --- |
| line.reference | The reference designator of the component |
| line.sub_part | The part at this position |
| line.quantity | The number of components |
| line.sub_part.build_order_allocations | ... |

