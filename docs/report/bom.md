---
title: BOM Generation
---

## BOM Generation
The bill of materials is an essential part of the documentation that needs to be send to the facctory. A sinple csv export is OK to be importet into SMT machines. But for human redable documentation it might not be suficcient. Additional information ist needed. The Inventree report system allows to generate BOM well formatted BOM reports. 

### A simple example
The following picture shows a simple example for a PCB with just three components from two different parts. 

{% with id="report-options", url="report/bom_example.png", description="Report Options" %} {% include 'img.html' %} {% endwith %}

This example has been created using the following html template:

```html
{% raw %}
{% extends "report/inventree_report_base.html" %}

{% load i18n %}
{% load report %}
{% load inventree_extras %}

{% block page_margin %}
margin-left: 2cm;
margin-right: 1cm;
margin-top: 4cm;
{% endblock %}

{% block bottom_left %}
content: "v{{report_revision}} - {{ date.isoformat }}";
{% endblock %}

{% block bottom_center %}
content: "InvenTree v{% inventree_version %}";
{% endblock %}

{% block style %}
.header-left {
    text-align: left;
    float: left;
}
table {
    border: 1px solid #eee;
    border-radius: 3px;
    border-collapse: collapse;
    width: 100%;
    font-size: 80%;
}
table td {
    border: 1px solid #eee;
}
{% endblock %}

{% block header_content %}
    <div class='header-left'>
        <h3>{% trans "Bill of Materials" %}</h3>
    </div>
{% endblock %}

{% block page_content %}
<table>
  <tr> <td>Board</td><td>{{ part.IPN }}</td>  </tr>
  <tr> <td>Description</td><td>{{ part.description }}</td> </tr>
  <tr> <td>User</td><td>{{ user }}</td> </tr>
  <tr> <td>Date</td><td>{{ date }}</td> </tr>
  <tr> <td>Number of different components (codes)</td><td>{{ bom_items.count }}</td> </tr>
</table>
<br>
<table class='table table-striped table-condensed'>
    <thead>
        <tr>
            <th>{% trans "IPN" %}</th>
            <th>{% trans "MPN" %}</th>
            <th>{% trans "Manufacturer" %}</th>
            <th>{% trans "Quantity" %}</th>
            <th>{% trans "Reference" %}</th>
            <th>{% trans "Substitute" %}</th>
        </tr>
    </thead>
    <tbody>
        {% for line in bom_items.all %}
          <tr>
            <td>{{ line.sub_part.IPN }}</td>
            <td>{{ line.sub_part.name }}</td>
	        <td>
	          {% for manf in line.sub_part.manufacturer_parts.all %}
               {{ manf.manufacturer.name }}
               {% endfor %}
          </td>
          <td>{% decimal line.quantity %}</td>
          <td>{{ line.reference }}</td>
	        <td>
	          {% for sub in line.substitutes.all %}
		    {{ sub.part.IPN }}<br>
            {% endfor %}
          </td>
          </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}
{% endraw %}
```

### Context variables
| Variable | Description |
| --- | --- |
| bom_items | Query set that contains all BOM items |
| bom_items...sub_part | One component of the BOM |
| bom_items...qualtity | Numeber of parts |
| bom_items...reference | Reference designators of the part |
| bom_items...substitutes | Query set that contains sunstitutes of the part if any exist in the BOM |
