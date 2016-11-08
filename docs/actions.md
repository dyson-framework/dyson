Actions
=======

There are multiple actions that can be taken on the application.
These "actions" are in the [core modules](https://github.com/dynamictivity/dyson-modules-core).

## Possible Actions

### Goto URL

> Go to a fully qualified URL

- `goto`
    - `url`
    
> Examples:

```yaml
- goto: url=https://google.com
```

---

### Click

> Click an element

- `click: <selector>` 

> Examples:

```yaml
- click: id=the_id
- click: name=btnSearch
```

---

### Check

> Checks a checkbox or radio button

- `check: <selector>`

> Examples:

```yaml
- check: id=checkbox
- check: tag=input
```

---

### Set Text

> Sets the value of an input

- `set_text`
    - `of`
    - `to`
    
> Examples:

```yaml
- set_text:
    of: name=q
    to: Search
```
