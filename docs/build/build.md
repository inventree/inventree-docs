---
title: Build
layout: page
---

## Building Parts

Build management can be accessed via the *Build* navigation tab.

A "basic" build flow is as follow:

1. create a part with the [*Assembly option*](/part/views/#part-options) turned-on
0. add a Bill of Material (BOM)
0. create a "Build Order" for this part
0. allocate stocks from your inventory
0. update build status and notes
0. complete the build.

##### Future Features

| Feature     | Status     	|
| ----------- | ----------- |
| Allow edit of completed builds | :material-progress-clock: [Work In Progress](https://github.com/inventree/InvenTree/pull/993)  |
| Track subparts used in build | :material-progress-clock: [Work In Progress](https://github.com/inventree/InvenTree/pull/991) |
| Partial build completion | :material-close: Not yet supported |

### Build Status

| Status | Description |
| ----------- | ----------- |
| `Pending` | "Build Order" has been created and build is ready for subpart allocation |
| `Allocated` | All subparts stocks in the part BOM have been allocated |
| `Cancelled` | Build has been cancelled |
| `Completed` | Build has been completed |

### Part BOM

A Part BOM is required to allocate inventory to a build.

Read through the [Bill of Materials documentation](/build/bom).

### Build Order

Builds orders are used to create parts builds.

To create a build order for your part, you have two options:

1. navigate to the Part detail page, click on "Build Orders" tab then click on "Start New Build" button
0. navigate to the Build page, click on "New Build Order"

{% with id="build_start_new", url="build/build_start_new.png", description="Start New Build Form" %}
{% include 'img.html' %}
{% endwith %}

Fill-out the form then click the "Submit" button to create the build.

### Stock Allocation

To allocate stock for a build, you have two options:

1. automatic allocation: if each subpart has only **one** storage location, InvenTree can allocate stock from this location automatically
0. manual allocation: user can define allocation for each subpart in the build

#### Automatic Allocation

Click on the "Allocated Parts tab" then click on the "Auto Allocate" button to automatically allocate stock.

#### Manual Allocation

Click on the "Allocated Parts tab" then click on the :fontawesome-solid-plus: icon next to each subpart in the build to manually allocate stock.

### Cancel Build

To cancel a build, click on :fontawesome-regular-times-circle: icon on the build detail page.

The `Cancel Build` form will be displayed, click on the confirmation switch then click on the "Cancel Build" button to process the build cancellation.

!!! warning "Cancelled Build"
	**A cancelled build cannot be re-opened**. Make sure to use the cancel option only if you are certain that the build won't be processed.

### Complete Build

To complete a build, click on :fontawesome-solid-tools: icon on the build detail page, the `Complete Build` form will be displayed.

!!! info "Incomplete Allocation"
	If the warning message `Warning: Build order allocation is not complete` is shown, make sure to allocate stock for the build before proceeding with build completion.

Select a `Location` to store the resulting parts from the build then click on the confirmation switch.
Finally, click on the "Complete Build" button to process the build completion.
