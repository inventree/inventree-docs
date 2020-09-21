---
title: Stock Test Result
layout: page
---

## Stock Test Result

Stock items which are associated with a *trackable* part can have associated test data - this is particularly useful for tracking unit testing / commissioning / acceptance data against a serialized stock item.

The master "Part" record for the stock item can define multiple [test templates](/part/test/), against which test data can be uploaded. Additionally, arbitrary test information can be assigned to the stock item.

!!! missing "TODO"
	Include pictures of the Test Results tab

### Test Result Fields

#### Test Name

The name of the test data is used to associate the test with a test template object.

#### Result

Boolean pass/fail status of the test.

#### Value

Optional value uploaded as part of the test data. For example if the test is to record the firmware version of a programmed device, the version number can be added here.

#### Notes

Optional field available for extra notes.

#### Attachment

A given test result may require an attached file which contains extra test information.

### Multiple Test Results

Multiple results can be uploaded against the same test name. In cases where multiple test results are uploaded, the most recent value is used to determine the pass/fail status of the test. It is useful to keep all test records as a given test might be required to run multiple times, if (for example) it fails the first time and then something must be fixed before running the test again.

### Reporting

!!! missing "TODO"
	Include information on the reporting plugin architecture

### Automated Test Intgration

The stock item testing framework is especially useful when integrating with an automated acceptance testing framework. Test results can be uploaded using the [InvenTree API](/extend/api/) or the [InvenTree Python Interface](/extend/python/).

!!! info "Example"
	You design and sell a temperature sensor which needs to be calibrated before it can be sold. An automated calibration tool sets the offset in the device, and uploads a test result to the InvenTree database.
