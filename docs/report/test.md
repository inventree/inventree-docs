---
title: Test Report
layout: page
---

## Test Report

InvenTree provides [test result](/stock/test) tracking functionality which allows the users to keep track of any tests which have been performed on a given stock item.

Custom test reports may be generated against any given stock item. All testing data is made available to the template for custom rendering as required.

For example, an "Acceptance Test" report template may be customized to the particular device, with the results for certain tests rendering in a particular part of the page, with any tests which have not passed highlighted.

!!! missing "TODO"
	This section requires further work

### Part Filters

A TestReport template may define a set of filters against which parts are sorted. Any Part objects which match the provided filters can use the given TestReport.

This allows each TestReport to easily be assigned to a particular Part, or even multiple parts.

In the example below, a test report template is uploaded and assigned to the part with the name *"My Widget"*. Any combination of fields relevent to the Part model can be used here.

{% with id="test_report_add", url="admin/test_report_add.png", description="Upload test report template" %}
{% include 'img.html' %}
{% endwith %}

### Context Variables

The following context variables are made available to the TestReport template for rendering:

- **stock_item**: The individual stock item for which this test report is being generated
- **part**: The Part of which the stock_item is an instance
- **results**: A dict of test result objects, where the 'key' for each test result is a shortened version of the test name (see below)
- **result_list**: A list of each test result object

#### Results

The *results* context variable provides a very convenient method of callout out a particular test result by name.

#### Example

Say for example that a Part "Electronic Widget" has a stock item with serial number #123, and has a test result uploaded called "Firmware Checksum". The templated file can reference this data as follows:

``` html
<h3>Part: {% raw %}{{ part.name }}{% endraw %}</h3>
<b>Serial Number: {% raw %}{{ stock_item.serial }}{% endraw %}</b>
<hr>
<p>
Firmware Checksum: {% raw %}{{ results.firmwarechecksum.value }}.
Uploaded by {{ results.firmwarechecksum.user }}{% endraw %}
</p>
```
