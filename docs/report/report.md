---
title: Report Generation
---

## Custom Reporting

InvenTree supports a customizable reporting ecosystem, allowing the user to develop reporting templates that meet their particular needs.

PDF reports are generated from custom HTML template files which are written by the user.

Reports are used in a variety of situations to format data in a friendly format for printing, distribution, conformance and testing.

In addition to providing the ability for end-users to provide their own reporting templates, some report types offer "built-in" report templates ready for use.

### WeasyPrint Templates

InvenTree report templates utilize the powerful [WeasyPrint](https://weasyprint.org/) PDF generation engine. 

!!! info "WeasyPrint"
    WeasyPrint is an extremely powerful and flexible reporting library. Refer to the [WeasyPrint docs](https://weasyprint.readthedocs.io/en/stable/) for further information.

### Stylesheets

Templates are rendered using standard HTML / CSS - if you are familiar with web page layout, you're ready to go!

### Template Language

Uploaded report template files are passed through the [django template rendering framework](https://docs.djangoproject.com/en/dev/topics/templates/), and as such accept the same variable template strings as any other django template file. Different variables are passed to the report template (based on the context of the report) and can be used to customize the contents of the generated PDF.

### Variables

Each report template is provided a set of *context variables* which can be used when rendering the template.

For example, rendering the name of a part (which is available in the particular template context as *part*) is as follows:

```html
{% raw %}

<!-- Template variables use {{ double_curly_braces }} -->
<h2>Part: {{ part.name }}</h3>
<p><i>
  Description:<br>
  {{ part.description }}
</p></i>
{% endraw %}
```

!!! info "Variables"
  	Templates will have different variables available to them depending on the report type. Read the detail information on each report type for further information.

### Context Data

Please refer to the [Context variables](./context_variables.md) page.

### Conditional Rendering

The django template system allows for conditional rendering, providing conditional flow statements such as `{% raw %}{% if <condition> %}{% endraw %}`, `{% raw %}{% for <item> in <list> %}{% endraw %}`, etc.

!!! info "Conditionals"
    Refer to the django documentation for more information.

## Report Options

A number of global reporting options are available for customizing InvenTree reports:

{% with id="report-options", url="report/report.png", description="Report Options" %}
{% include 'img.html' %}
{% endwith %}

### Enable Reports

By default, the reporting feature is turned off. It must be enabled in the global settings. 


### Default Page Size

The built-in InvenTree report templates (and any reports which are derived from the built-in templates) use the *Page Size* option to set the page size of the generated reports.

!!! info "Override Page Size"
    Custom report templates do not have to make use of the *Page Size* option, although it is made available to the template context.

### Debug Mode

As templates are rendered directly to a PDF object, it can be difficult to debug problems when the PDF does not render exactly as expected. 

Setting the *Debug Mode* option renders the template as raw HTML instead of PDF, allowing the rendering output to be introspected. This feature allows template designers to understand any issues with the generated HTML (before it is passed to the PDF generation engine).

!!! warning "HTML Rendering Limitations"
    When rendered in debug mode, @page attributes (such as size, etc) will **not** be observed. Additionally, any asset files stored on the InvenTree server will not be rendered. Debug mode is not intended to produce "good looking" documents!

## Uploading Templates

Custom report templates can be uploaded using the [Admin Interface(../settings/admin.md). Only users with admin access can upload and/or edit report template files.

## Report Assets

User can upload asset files (e.g. images) which can be used when generating reports. For example, you may wish to generate a report with your company logo in the header. Asset files are uploaded via the admin interface.

Asset files can be rendered directly into the template as follows

```html
{% raw %}
<!-- Need to include the report template tags at the start of the template file -->
{% load report %}

<!-- Simple stylesheet -->
<head>
  <style>
    .company-logo {
      height: 50px;
    }
  </style>
</head>

<body>
<!-- Report template code here -->

<!-- Render an uploaded asset image -->
<img src="{% asset 'company_image.png' %}" class="company-logo">

<!-- ... -->
</body>

{% endraw %}
```

!!! warning "Asset Naming"
    If the requested asset name does not match the name of an uploaded asset, the template will continue without loading the image.

## Report Snippets

A powerful feature provided by the django / WeasyPrint templating framework is the ability to include external template files. This allows commonly used template features to be broken out into separate files and re-used across multiple templates.

To support this, InvenTree provides report "snippets" - short (or not so short) template files which cannot be rendered by themselves, but can be called from other templates.

Similar to assets files, snippet template files are uploaded via the admin interface.

Snippets are included in a template as follows:

```
{% raw %}{% include 'snippets/<snippet_name.html>' %}{% endraw %}
```

For example, consider a stocktake report for a particular stock location, where we wish to render a table with a row for each item in that location.

```html
{% raw %}

<table class='stock-table'>
  <thead>
    <!-- table header data -->
  </thead>
  <tbody>
    {% for item in location.stock_items %}
    {% include 'snippets/stock_row.html' with item=item %}
    {% endfor %}
  </tbody>

{% endraw %}
```

!!! info "Snippet Arguments"
    Note above that named argument variables can be passed through to the snippet!

And the snippet file `stock_row.html` is as follows:

```html
{% raw %}
<!-- stock_row snippet -->
<tr>
  <td>{{ item.part.full_name }}</td>
  <td>{{ item.quantity }}</td>
</tr>
{% endraw %}
```

## Report Types

InvenTree supports the following reporting functionality:

### Test Report

[Test Report](./test.md): Format results of a test report against for a particular StockItem

### Packing List
[Packing List](./pack.md): Format a list of items for shipping or transfer

### Build Report

[Build Order](./build.md): Format a build order report

### Purchase Order
[Purchase Order report](./order.md): Order line items 

### Sales Order
Sales Order: TODO

### Stocktake
Stocktake Report: TODO
