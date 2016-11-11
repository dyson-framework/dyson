Getting Started with Dyson
==========================

## Create your first test

- Create the following directory structure:

```
first-dyson-project/
  dyson.cfg
  apps/
    default.yml
  tests/
    basic/
      steps/
        main.yml
```

- Put the [source from the sample](https://github.com/dynamictivity/dyson/tree/master/sample/dyson.cfg) inside of `dyson.cfg`

- Inside of `apps/default.yml`:

```yaml
---

app_url: {{ http.protocol }}://google.com
```

- Inside of `steps/main.yml`:

```yaml
---

- name: navigate to the url
  goto: "url={{ app_url }}"
  
- validate: title=Google
```

- Run `$ dyson-test tests/basic`

**Now...** Let's discuss what just happened.

Dyson at it's core, is just a wrapper around Selenium WebDriver.
As you can see, the test that you just wrote is powered entirely by YAML. (JSON also works, too)

Let's look at this step by step.

> `app_url: {{ http.protocol }}://google.com`

This defines a variable that all of the tests can use. Dyson uses [Jinja](http://jinja.pocoo.org/) for variable rendering,
so `app_url` will be whatever `http.protocol` is, plus `://google.com` - See [Variables](https://github.com/Dynamictivity/dyson/blob/master/docs/variables.md)

The `http.protocol` is set within `dyson.cfg`, under the `[http]` section.

Each Dyson test is a collection of steps.  In `steps/main.yml`, you can see that the test is
a YAML array.  These are the steps that your test will take.

> ```yaml
    name: navigate to the url
    goto: "url={{ app_url }}"
  ```
  
Here, we just told Dyson to go to the url, `{{ app_url }}`.  The `app_url` is what we specified in `apps/default.yml`.

We then validated that the URL is "Google".
