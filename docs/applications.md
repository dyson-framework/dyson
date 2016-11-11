Applications
============

> `apps/`


## Design

In the application directory, you are able to specify any number of environments.
These environments are defined in yaml or json dictionaries, and are **always**
objects, not arrays.

In the application directory, it is required that you have at least `default.yml`.

The `default.yml` application represents any variable that you may need in your tests.

You may also create additional environments as needed to override those set in `default.yml`.

A typical application directory would look like:

```
apps/
  default.yml
  test.yml
  production.yml
```

## Specifying an environment

You may specify an environment by passing `-a <app>.yml` or `--application <app>.yml`.

## Example

Consider the following applications.

**default.yml**

```yaml
---
application_url: "http://localhost:3000"

# Login Page objects
login_page:
  txt_username: css=#username
  txt_password: css=#password
  btn_submit: id=submit
```

**production.yml**

```yaml
---
application_url: "https://application.com"
```

By specifying `-a production.yml` into Dyson, two things will happen:

- Dyson will load in the variables from `default.yml`
- Dyson will then load your application.yml file in, and override any variables specified in
`default.yml` with those specified in `production.yml`

