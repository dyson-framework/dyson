Actions
=======

There are multiple actions that can be taken on the application.
These "actions" are in the [core modules](https://github.com/dynamictivity/dyson-modules-core).

- [Goto URL](#goto-url)
- [Click](#click)
- [Check](#check)
- [Uncheck](#uncheck)
- [Set Text](#set-text) 
- [Switch To...](#switch-to)
  * [Switch to Frame](#switch-to-frame)
  * [Switch to Alert](#switch-to-alert) 
  * [Switch to Window](#switch-to-window)

---

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

### Uncheck

> Unchecks **only** a checkbox

- `uncheck: <selector>`

> Examples:

```yaml
- uncheck: css=some > css.selector
- uncheck:
    id: some_id
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

### Switch To...

- `switch_to`
    - `frame`
    - `alert`
    - `window`

#### Switch to frame

```yaml
- switch_to:
    frame: id=framename
```

#### Switch to alert

- [See alerts.md](https://github.com/dynamictivity/dyson/tree/master/docs/alerts.md#alerts) 

#### Switch to window

```yaml
- switch_to:
    window: 0  # -1 for last window opened
```
