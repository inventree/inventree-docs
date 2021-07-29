---
title: Context Variables
---

## Context Variables

Context variables are available when creating templates for reports. These context variables will be filled with information about a particular report or even a part or stock location.

### Build

In addition to the default report context variables, the following context variables are made available to the build order report template for rendering:

| Variable | Description |
| --- | --- |
| build | The build object the report is being generated against |
| part | The part object that the build references |
| reference | The build order reference string |
| quantity | Build order quantity |

### Part


