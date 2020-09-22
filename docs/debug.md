---
title: Debug
layout: page
---

## Debug

### Readthedocs

*[Reference](https://docs.readthedocs.io/en/stable/development/design/theme-context.html#context-injected)*

{{ readthedocs }}

### Mkdocs

#### Base URL

base_url: `{{ base_url }}`

#### Environment

{{ context(environment) | pretty }}

#### Global Variables

{{ context(extra) | pretty }}

#### Config

{{ context(config) | pretty }}