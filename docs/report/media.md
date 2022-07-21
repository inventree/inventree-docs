---
title: Using media files
---

## Images

To load images into the reports/labels the report helper must be loaded in the template. 

```html
{% raw %}
<!-- Load the report helper functions -->
{% load report %}
{% endraw %}
```

### Assets

You can add images to the reports and labels by using the asset template tag:

```html
{% raw %}
<!-- Load the report helper functions -->
{% load report %}
<img src="{% asset 'my_awesome_logo.png' %}"/>
{% endraw %}
```

!!! info "Assets location"
    You need to place your asset images to the report/assets directory in the [data directory](../start/docker_dev.md/#data-directory)

### Part images

You can render the images of the parts using the part_image template tag:

```html
{% raw %}
<!-- Load the report helper functions -->
{% load report %}
<img src='{% part_image part %}'/>
{% endraw %}
```
