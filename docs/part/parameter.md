---
title: Part Parameters
layout: page
--- 

## Part Parameters

Part parameters are located in the "Parameters" tab, on each part detail page.
There is no limit for the number of part parameters and they are fully customizable through the use of parameters templates.

Here is an example of parameters for a Ceramic capacitor:
{% with id="part_parameters_example", url="part/part_parameters_example.png", description="Part Parameters Example List" %}
{% include 'img.html' %}
{% endwith %}

### Create Template

A *Parameter Template* is required for each part parameter.

To create a template, you have two options:

1. navigate to the "Settings" page, click on the "Part" tab and then click on the "New Parameter" button
0. navigate to a specific part detail page, click on the "Parameters" tab, click on the "New Parameters" button then click on the "New Template" button in the newly displayed form.

The `Create Part Parameter Template` form will be displayed:
{% with id="create_parameter_template", url="part/create_parameter_template.png", description="Create Part Parameter Template Form" %}
{% include 'img.html' %}
{% endwith %}

Fill-out the template `Name` (required) and `Units` (optional) fields then click the "Submit" button.

### Create Parameter

After [creating a template](#create-template) or using the existing templates, you can add parameters to any part.

To add a parameter, navigate to a specific part detail page, click on the "Parameters" tab then click on the "New Parameters" button, the `Create Part Parameter` form will be displayed:

{% with id="create_part_parameter", url="part/create_part_parameter.png", description="Create Part Parameter Form" %}
{% include 'img.html' %}
{% endwith %}

Select the parameter `Template` you would like to use for this parameter, fill-out the `Data` field (value of this specific parameter) and click the "Submit" button.

### Parametric Tables

!!! note "Future Feature Proposal"
	Allow parts to be filtered using parameters. Narrow down the list of parameters to the parts found in each category.
