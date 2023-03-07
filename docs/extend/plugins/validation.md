---
title: Validation Mixin
---

## ValidationMixin

The `ValidationMixin` class enables plugins to perform custom validation of various fields.

Any of the methods described below can be implemented in a custom plugin to provide functionality as required.

!!! info "More Info"
    For more information on any of the methods described below, refer to the InvenTree source code.

!!! info "Multi Plugin Support"
    It is possible to have multiple plugins loaded simultaneously which support validation methods. For example when validating a field, if one plugin returns a null value (`None`) then the *next* plugin (if available) will be queried.

### Part Name

By default, part names are not subject to any particular naming conventions or requirements. However if custom validation is required, the `validate_part_name` method can be implemente to ensure that a part name conforms to a required convention.

If the custom method determines that the part name is *objectionable*, it should throw a `ValidationError` which will be handled upstream by parent calling methods.

### Part IPN

Validation of the Part IPN (Internal Part Number) field is exposed to custom plugins via the `validate_part_IPN` method. Any plugins which extend the `ValidationMixin` class can implement this method, and raise a `ValidationError` if the IPN value does not match a required convention.

### Batch Codes

[Batch codes](../../stock/tracking.md#batch-codes) can be generated and/or validated by custom plugins.

The `validate_batch_code` method allows plugins to raise an error if a batch code input by the user does not meet a particular pattern.

The `generate_batch_code` method can be implemented to generate a new batch code.

### Serial Numbers

Requirements for serial numbers can vary greatly depending on the application. Rather than attempting to provide a "one size fits all" serial number implementation, InvenTree allows custom serial number schemes to be implemented via plugins.

The default InvenTree [serial numbering system](../../stock/tracking.md#serial-numbers) uses a simple algorithm to validate and increment serial numbers. More complex behaviours can be implemented using the `ValidationMixin` plugin class and the following custom methods:

#### Serial Number Validation

Custom serial number validation can be implemented using the `validate_serial_number` method. A *proposed* serial number is passed to this method, which then has the opportunity to raise a `ValidationError` to indicate that the serial number is not valid.

##### Example

A plugin which requires all serial numbers to be valid hexadecimal values may implement this method as follows:

```python
def validate_serial_number(self, serial: str, part: Part):
    """Validate the supplied serial number
    
    Arguments:
        serial: The proposed serial number (string)
        part: The Part instance for which this serial number is being validated
    """

    try:
        # Attempt integer conversion
        int(serial, 16)
    except ValueError:
        raise ValidationError("Serial number must be a valid hex value")
```

#### Serial Number Sorting

While InvenTree supports arbitrary text values in the serial number fields, behind the scenes it attempts to "coerce" these values into an integer representation for more efficient sorting.

A custom plugin can implement the `convert_serial_to_int` method to determine how a particular serial number is converted to an integer representation.

!!! info "Not Required"
    If this method is not implemented, or the serial number cannot be converted to an integer, then the sorting algorithm falls back to the text (string) value

#### Serial Number Incrementing

A core component of the InvenTree serial number system is the ability to *increment* serial numbers - to determine the *next* serial number value in a sequence. 

For custom serial number schemes, it is important to provide a method to generate the *next* serial number given a current value. The `increment_serial_number` method can be implemented by a plugin to achieve this.

!!! info "Invalid Increment"
    If the provided number cannot be incremented (or an error occurs) the method should return `None`

##### Example

Continuing with the hexadecimal example as above, the method may be implemented as follows:

```python
def increment_serial_number(self, serial: str):
    """Provide the next hexadecimal number in sequence"""

    try:
        val = int(serial, 16) + 1
        val = hex(val).upper()[2:]
    except ValueError:
        val = None

    return val
```
