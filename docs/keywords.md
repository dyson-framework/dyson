Keywords
========

Keywords are a set of steps to execute in your tests and can be called just
like a [module](https://github.com/dynamictivity/dyson/tree/master/docs/modules.md) is called.

There are two locations that keywords may reside.

- In your project root, a subdirectory named `keywords/`
- In specific test directories, a subdirectory named `keywords/`

## Create your first keyword

Consider a scenario in your application where you would like to wait until
the element you would like to click is present before you click on it.
 
You can accomplish this task by using keywords.

Create a file named `wait_then_click.yml` inside of `keywords/`

**wait_then_click.yml**

```yaml
- wait_for:
    clickable: "element={{ wait_then_click.element }}"
    
- click: "{{ wait_then_click.element }}"
```

In your test, you may then call your keyword just as you would a module.

**tests/<test>/main.yml**

```yaml
- goto: url=http://google.com

- wait_then_click: "element={{ my_element }}"
```

Note that in the keyword, we are using `wait_then_click.element`.  The way
keywords work is Dyson will pass any variable you specify from your test, into
the keyword.  The variables passed into the keyword will reside inside of the
keyword object.  In our case, our keyword is `wait_then_click` hence we use `wait_then_click`

If we didn't need a dictionary, we can specify simply a string and access it like such:

**keywords/my_keyword.yml**

```yaml
- validate: "title={{ my_keyword }}"
```

Since `my_keyword` represents what was passed in from the test, we can simply do:

```yaml
- my_keyword: Google
```

## Keyword Overrides

Just as modules do, keywords also override modules provided by Dyson. This means that you can create
a keyword called `click.yml`, and it will override the core `click` module.  **Be wary of this!**
