---
title: Packing List Report
---

## Packing List

!!! missing "TODO"
	This section requires further work

## Pick List

When all material has been allocated someone has to pick all things from the warehouse. 
In case you need a printed pick list you can use the following template. This it just the 
table. All other info and CSS has been left out for simplicity. Please have a look at the 
BOM report for details.

{% raw %}
```html
<table class='changes-table'>
  <thead>
    <tr>
      <th>Original IPN</th>
      <th>Allocated Part</th>
      <th>Location</th>
      <th>PCS</th>
    </tr>
  </thead>
  <tbody>
  {% for line in build.allocated_stock.all %}
    <tr>
      <td> {{ line.bom_item.sub_part.IPN }} </td>
      {% if line.stock_item.part.IPN != line.bom_item.sub_part.IPN %}
        <td class='chg'> {{ line.stock_item.part.IPN }} </td>
      {% else %}
        <td> {{ line.stock_item.part.IPN }} </td>
      {% endif %}
      <td> {{ line.stock_item.location.pathstring }} </td>
      <td> {{ line.quantity }} </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
```
{% endraw %}

Here we have a loop that runs through all allocated parts for the build. For each part
we list the original IPN from the BOM and the IPN of the allocated part. These can differ
in case you have substitutes or template/variants in the BOM. In case the parts differ
we use a different format for the table cell e.g. print bold font or red color. 
For the picker we list the full path names of the stock locations and the quantity
that is needed for the build. This will result in the following printout:

{% with id="report-options", url="report/picklist.png", description="Picklist Example" %} {% include "img.html" %} {% endwith %}

