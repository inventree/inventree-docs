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

bom_items that can be looped using 

```html 
{%for line in build.bom_items %}
some code
{% endfor %}
```

Each bom_item line has further context variables.

| Variable | Description |
| --- | --- |
| line.reference | The reference designator of the component |
| line.sub_part | The part at this position |
| line.quantity | The number of components |
| line.sub_part.build_order_allocations | ... |

A very simple example wihtout any html formatting:

```html
reference: {{reference }} 
<br>
quantity: {{ quantity }} 
<br>
title: {{ title }} 
<br>
part: {{ part }} 
<br>
build: {{ build }} 
<br>
<br>
build.reference: {{ build.reference }} 
<br>
build.title: {{ build.title }} 
<br>
build.status: {{ build.status }} 
<br>
-------
<br>
{% for line in build.bom_items %}
reference:: {{ line.reference }} 
<br>
quantity:: {{ line.quantity }} 
<br>
sub_part: {{ line.sub_part }} 
<br>
sub_part.IPN: {{ line.sub_part.IPN }} 
<br>
sub_part.name: {{ line.sub_part.name }} 
<br>
sub_part.build_order_allocations: {{ line.sub_part.build_order_allocations }} 
<br>
........
<br>
{% endfor %}
```

This will result in:

```text
reference: 0001
quantity: 10
title: BO0001
part: POP-000001-001 | Converter - A to B
build: BO0001

build.reference: 0001
build.title: Description of the build
build.status: 20
-------
reference:: U002
quantity:: 1.00000
sub_part: ANA-000001-001 | op701 - operation amplifier
sub_part.IPN: ANA-000001-001
sub_part.name: op701
sub_part.build_order_allocations: <QuerySet [<BuildItem: BuildItem object (9)>]>
........
reference:: U001
quantity:: 2.00000
sub_part: ANA-000002-001 | L7805 - LDO
sub_part.IPN: ANA-000002-001
sub_part.name: L7805
sub_part.build_order_allocations: <QuerySet [<BuildItem: BuildItem object (5)>]>
........ 
```
