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

#### build 

| Variable | Description |
| --- | --- |
| title | The full name of the build |
| quantity | Build order quantity |
| title | The description of the build |
| status | The status of the build. 20 means 'Production' |
| bom_items | A query set with all bom items for the build |
| required_parts | A query set with all bom items for the build |
| sub_build_count | Number of sub builds |
| sub_builds | Query set with all sub builds |
| is_overdue | Boolean that tells if the build is overdue |
| active | Boolean that tells if the build is active |
| can_complete | Boolean that tells if the build can be completed ( all material allocated)|
| is_complete | Boolean that tells if the build is complete |
| parent | parent build if this is a sub build |
| target_date | Date where the build should be finished |
| creation_date | Date where the build has been created |
| issued_by | User who created the build |
| responsible | User who is responsible for the build |

As usual items in a query sets can be selected by adding a .n to the set e.g. build.required_parts.0
will result in the first part of the list. Each query set has again its own context variables.

#### bom_items 

| Variable | Description |
| --- | --- |
| .reference | The reference designators of the components |
| .quantity | The number of components |
| .sub_part | The part at this position |
| .substitutes.all | A query set with all allowed substitutes for that part |

### Example 

A very simple example without any html formatting:

{% raw %}
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
{% endraw %}
