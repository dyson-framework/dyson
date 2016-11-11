Variables
====================

There are four possible ways to specify variables within your tests
and are overriden in this order:

1. `apps/default.yml`
2. `apps/<application>.yml`
3. `tests/<test>/vars/main.yml`
4. `-e "my_variable=something another_variable=something_else"`

## Example

Consider the following:

**apps/default.yml**

```yaml
---
application_url: http://localhost:3000

login_page:
  txt_username: css=#username
```

**apps/production.yml**

```yaml
---
application_url: https://productionurl.com

login_page:
  txt_username: "{{ login_page.txt_username }}-production"
```

**tests/&lt;test&gt;/vars/main.yml**

```yaml
---
test_url: "{{ application_url }}/some/path"
```

**`-e "test_url=http://anotherurl.com/some/path"`**

At the time of execution:

- `application_url` will be `https://productionurl.com` since `production.yml`
will override what is set in `defaults.yml`
- `test_url` will be `https://productionurl.com/`
- `login_page.txt_username` will be `css=#username-production`

## Accessing Variables

From the [examples above](#examples), you can see that we are able to access
variables by using `{{ ... }}` notation.  This is [Jinja](http://jinja.pocoo.org/).
You are able to reference these variables anywhere in your tests, or your other variable
files.

All variables are able to be overridden in the presedence [noted above](#variables).
