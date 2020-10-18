---
title: InvenTree API
---

## InvenTree API

InvenTree provides a powerful REST API for interacting with inventory data on the server. Low-level data access and manipulation is available, with integrated user authentication and data validation

## Documentation

The API is self-documenting, and the documentation is provided alongside any InvenTree installation instance. If (for example) you have an InvenTree instance running at `http://127.0.0.1:8000` then the API documentation is available at `http://127.0.0.1:8000/api-doc/`

{% with id="api_doc", url="api/api_doc.png", description="API documentation" %}
{% include 'img.html' %}
{% endwith %}

## Authentication

Users must be authenticated to gain access to the InvenTree API. The API accepts either basic username:password authentication, or token authentication. Token authentication is recommended as it provides much faster API access.

!!! warning "Permissions"
    API access is restricted based on the permissions assigned to the user.

### Tokens

Each user is assigned an authentication token which can be used to access the API. This token is persistent for that user (unless invalidated by an administrator) and can be used across multiple sessions.

!!! info "Token Administration"
    User tokens can be created and/or invalidated via the Admin interface.

### Requesting a Token

If a user does not know their access token, it can be requested via the API interface itself, using a basic authentication request.

To obtain a valid token, perform a GET request to `/api/user/token/`. No data are required, but a valid username / password combination must be supplied in the authentication headers.

!!! info "Credentials"
	Ensure that a valid username:password combination are supplied as basic authorization headers.

Once a valid token is received from the server, subsequent API requests should be performed using that token.

If the supplied user credentials are validated, the server will respond with:

```
HTTP_200_OK
{
    token: "usertokendatastring",
}
```

### Using a Token

After reception of a valid authentication token, it can be subsequently used to perform token-based authentication.

The token value sent to the server must be of the format `Token <TOKEN-VALUE>` (without the < and > characters).

**Example: Javascript**
```javascript
var token = "MY-TOKEN-VALUE-HERE";

$.ajax({
  url: "http://localhost:8080/api/part/",
  type: 'GET',
  headers: {"Authorization": `Token ${token}`}
});
```

**Example: Python (Requests)**
```python
import requests

token = 'MY-TOKEN-VALUE-HERE'
data = { ... }
headers = {
    'AUTHORIZATION': f'Token {token}'
}
response = request.get('http://localhost:8080/api/part/', data=data, headers=headers)
```