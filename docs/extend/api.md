---
title: InvenTree API
layout: page
---

## InvenTree API

InvenTree provides a powerful REST API for interacting with inventory data on the server. Low-level data access and manipulation is available, with integrated user authentication and data validation

### Documentation

The API is self-documenting, and the documentation is provided alongside any InvenTree installation instance. If (for example) you have an InvenTree instance running at `http://127.0.0.1:8000` then the API documentation is available at `http://127.0.0.1:8000/api-doc/`

{% with id="api_doc", url="api/api_doc.png", description="API documentation" %}
{% include 'img.html' %}
{% endwith %}

### Authentication

The API uses token-based authentication for fast data access. To obtain a valid token, perform a GET request to `/api/user/token/` (no data are required).

!!! info "Credentials"
	Ensure that a valid username:password combination are supplied as basic authorization headers.

If the supplied user credentials are validated, the server will respond with:

```
HTTP_200_OK
{
    token: "usertokendatastring",
}
```

After reception of a valid authentication token, it can be subsequently used to perform token-based authentication.