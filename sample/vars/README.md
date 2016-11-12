Project-Wide Test variables
===========================

In this directory, you are able to create any number of var files that
can be shared between all tests.

A common use for this directory would be to map out pages.

For example:

```yaml
---
# vars/login_page.yml

login_page:
  txt_username: id=username
  txt_password: id=password
  # ...
```

```yaml
# vars/register_page.yml

register_page:
  txt_firstname: id=firstname
  txt_lastname: id=lastname
  # ...
```
