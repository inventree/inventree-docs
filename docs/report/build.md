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
| build | The build object the report is being generated against |
| part | The [Part](./context_variables.md#part) object that the build references |
| reference | The build order reference string |
| quantity | Build order quantity |

#### build 

The following variables are accessed by build.variable

| Variable | Description |
| --- | --- |
| active | Boolean that tells if the build is active |
| batch | Batch code transferred to build parts (optional) |
| bom_items | A query set with all BOM items for the build |
| can_complete | Boolean that tells if the build can be completed ( all material allocated)|
| creation_date | Date where the build has been created |
| completion_date | Date the build was completed (or, if incomplete, the expected date of completion) |
| completed_by | User that completed the build |
| is_overdue | Boolean that tells if the build is overdue |
| is_complete | Boolean that tells if the build is complete |
| issued_by | User who created the build |
| link | External URL for extra information | 
| notes | Text notes |
| parent | Reference to a parent build object if this is a sub build |
| part | The [Part](./context_variables.md#part) to be built (from component BOM items) |
| quantity | Build order quantity |
| reference | Build order reference (required, must be unique) |
| required_parts | A query set with all parts that are required for the build |
| responsible | User (or group) responsible for completing the build |
| sales_order | References to a [Sales Order](./context_variables.md#salesorder) object for which this build is required (e.g. the output of this build will be used to fulfil a sales order) |
| status | The status of the build. 20 means 'Production' |
| sub_build_count | Number of sub builds |
| sub_builds | Query set with all sub builds |
| target_date | Date the build will be overdue |
| take_from | [StockLocation](./context_variables.md#stocklocation) to take stock from to make this build (if blank, can take from anywhere) |
| title | The full name of the build |
| title | The description of the build |
| allocated_stock.all | A query set with all allocated stock items for the build |

As usual items in a query sets can be selected by adding a .n to the set e.g. build.required_parts.0
will result in the first part of the list. Each query set has again its own context variables.

#### bom_items 

| Variable | Description |
| --- | --- |
| .reference | The reference designators of the components |
| .quantity | The number of components |
| .sub_part | The part at this position |
| .substitutes.all | A query set with all allowed substitutes for that part |


#### allocated_stock.all 

| Variable | Description |
| --- | --- |
| .bom_item | The bom item where this part belongs to |
| .stock_item | The allocated [StockItem](./context_variables.md#stockitem) |

### Example 

The following example will create a report with header and BOM. In the BOM table substitutes will be listed. 

{% raw %}
```html
{% extends "report/inventree_report_base.html" %}

{% load i18n %}
{% load report %}
{% load barcode %}
{% load inventree_extras %}
{% load markdownify %}

{% block page_margin %}
margin: 2cm;
margin-top: 4cm;
{% endblock %}

{% block style %}

.header-right {
    text-align: right;
    float: right;
}

.logo {
    height: 20mm;
    vertical-align: middle;
}

.details {
    width: 100%;
    border: 1px solid;
    border-radius: 3px;
    padding: 5px;
    min-height: 42mm;
}

.details table {
    overflow-wrap: break-word;
    word-wrap: break-word;
    width: 65%;
    table-layout: fixed;
    font-size: 75%;
}
.changes table {
    overflow-wrap: break-word;
    word-wrap: break-word;
    width: 100%;
    table-layout: fixed;
    font-size: 75%;
    border: 1px solid;
}

.changes-table th {
    font-size: 100%;
    border: 1px solid;
}

.changes-table td {
    border: 1px solid;
}

.details table td:not(:last-child){
    white-space: nowrap;
}

.details table td:last-child{
    width: 50%;
    padding-left: 1cm;
    padding-right: 1cm;
}

.details-table td {
    padding-left: 10px;
    padding-top: 5px;
    padding-bottom: 5px;
    border-bottom: 1px solid #555;
}

{% endblock %}

{% block bottom_left %}
content: "v{{report_revision}} - {{ date.isoformat }}";
{% endblock %}

{% block header_content %}
    <!-- TODO - Make the company logo asset generic -->
    <img class='logo' src="{% asset 'company_logo.png' %}" alt="logo" width="150">

    <div class='header-right'>
        <h3>
            Build Order {{ build }}
        </h3>
        <br>
    </div>

    <hr>
{% endblock %}

{% block page_content %}

<div class='details'>

        <table class='details-table'>
            <tr>
                <th>{% trans "Build Order" %}</th>
                <td>{% internal_link build.get_absolute_url build %}</td>
            </tr>
            <tr>
                <th>{% trans "Order" %}</th>
                <td>{{ reference }}</td>
            </tr>
            <tr>
                <th>{% trans "Part" %}</th>
                <td>{% internal_link part.get_absolute_url part.IPN %}</td>
            </tr>
            <tr>
                <th>{% trans "Quantity" %}</th>
                <td>{{ build.quantity }}</td>
            </tr>
            <tr>
                <th>{% trans "Description" %}</th>
                <td>{{ build.title }}</td>
            </tr>
            <tr>
                <th>{% trans "Issued" %}</th>
                <td>{% render_date build.creation_date %}</td>
            </tr>
            <tr>
                <th>{% trans "Target Date" %}</th>
                <td>
                    {% if build.target_date %}
                    {% render_date build.target_date %}
                    {% else %}
                    <em>Not specified</em>
                    {% endif %}
                </td>
            </tr>
            {% if build.parent %}
            <tr>
                <th>{% trans "Required For" %}</th>
                <td>{% internal_link build.parent.get_absolute_url build.parent %}</td>
            </tr>
            {% endif %}
            {% if build.issued_by %}
            <tr>
                <th>{% trans "Issued By" %}</th>
                <td>{{ build.issued_by }}</td>
            </tr>
            {% endif %}
            {% if build.responsible %}
            <tr>
                <th>{% trans "Responsible" %}</th>
                <td>{{ build.responsible }}</td>
            </tr>
            {% endif %}
            <tr>
                <th>{% trans "Sub builds count" %}</th>
                <td>{{ build.sub_build_count }}</td>
            </tr>
	    {% if build.sub_build_count > 0 %}
            <tr>
                <th>{% trans "Sub Builds" %}</th>
                <td>{{ build.sub_builds }}</td>
            </tr>
            {% endif %}
            <tr>
                <th>{% trans "Overdue" %}</th>
                <td>{{ build.is_overdue }}</td>
            </tr>
            <tr>
                <th>{% trans "Can complete" %}</th>
                <td>{{ build.can_complete }}</td>
            </tr>
        </table>
</div>

<h3>{% trans "Notes" %}</h3>
{% if build.notes %}
{{ build.notes|markdownify }}
{% endif %}

<h3>{% trans "Parts" %}</h3>

<div class='changes'>
  <table class='changes-table'>
    <thead>
      <tr>
	<th>Original IPN</th>
	<th>Reference</th>
	<th>Replace width IPN</th>
      </tr>
    </thead>
    <tbody>
  {% for line in build.bom_items %}
      <tr>
	<td> {{ line.sub_part.IPN }} </td>
	<td> {{ line.reference }} </td>
	<td> {{ line.substitutes.all.0.part.IPN }} </td>
      </tr>
  {% endfor %}
    </tbody>
  </table>
</div>
{% endblock %}
```

{% endraw %}

This will result a report page like this:

{% with id="report-options", url="build/report-61.png", description="Report Example Builds" %} {% include "img.html" %} {% endwith %}

