---
title: Stock Tracking
---

## Stock Tracking

It may be desirable to track individual stock items, or groups of stock items, with unique identifier values. Stock items may be *tracked* using either *Batch Codes* or *Serial Numbers*.

Individual stock items can be assigned a batch code, or a serial number, or both, or neither, as requirements dictate.

{% with id="batch_and_serial", url="stock/batch_and_serial.png", description="Batch and serial number" %}
{% include 'img.html' %}
{% endwith %}

Out of the box, the default implementations for both batch codes and serial numbers are (intentionally) simplistic.

As the particular requirements for serial number or batch code conventions may vary significantly from one application to another, InvenTree provides the ability for custom plugins to determine exactly how batch codes and serial numbers are implemented.

### Batch Codes

Batch codes can be used to specify a particular "group" of items, and can be assigned to any stock item without restriction. Batch codes are tracked even as stock items are split into separate items.

Multiple stock items may share the same batch code without restriction, even across different parts.

#### Generating Batch Codes

Batch codes can be generated automatically based on a provided pattern. The default pattern simply uses the current datecode as the batch number, however this can be customized within a certain scope.

{% with id="batch_code_pattern", url="stock/batch_code_template.png", description="Batch code pattern" %}
{% include 'img.html' %}
{% endwith %}

#### Plugin Support

To implement custom batch code functionality, refer to the details on the [Validation Plugin Mixin](../extend/plugins/validation.md#batch-codes).

### Serial Numbers

A serial "number" is used to uniquely identify a single, unique stock item. Note that while *number* is used throughout the documentation, these values are not required to be numeric.

#### Uniqueness Requirements

By default, serial numbers must be unique across any given [Part](../part/part.md) instance (including any variants of that part).

However, it is also possible to specify that serial numbers must be globally unique across all types of parts. This is configurable in the settings display (see below):

{% with id="serial_numbers_unique", url="stock/serial_numbers_unique.png", description="Serial number uniqueness" %}
{% include 'img.html' %}
{% endwith %}

#### Generating Serial Numbers

In the default implementation, InvenTree assumes that serial "numbers" are integer values in a simple incrementing sequence e.g. `{1, 2, 3, 4, 5, 6}`. When generating the *next* value for a serial number, the algorithm looks for the *most recent* serial number, and attempts to coerce that value into an integer, and then increment that value.

While this approach is reasonably robust, it is definitely simplistic and is not expected to meet the requirements of every installation. For this reason, more complex serial number management is intented to be implemented using a custom plugin (see below).

#### Plugin Support

Custom serial number functionality, with any arbitrary requirements or level of complexity, can be implemented using the [Validation Plugin Mixin class](../extend/plugins/validation.md#serial-numbers). Refer to the documentation for this plugin for technical details.

A custom plugin allows the user to determine how a "valid" serial number is defined, and (crucially) how any given serial number value is incremented to provide the next value in the sequence.

Implementing custom methods for these two consideraions allows for complex serial number schema to be supported with minimal effort.
