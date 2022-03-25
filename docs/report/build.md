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
| reference | The build order reference string |
| quantity | Build order quantity |



