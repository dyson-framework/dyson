Dyson Validations
=================

There are many validations bundled in the [core modules](https://github.com/dynamictivity/dyson-modules-core)
which will perform validations.

The validation module has many variations of validations it can perform.

- `validate`
    - `title`
        - `is`
        - `is_not`
    - `text_of`
        - `element`
            - `is`
            - `is_not`
    - `present <selector>`
    - `not_present <selector>`
    - `value_of`
        - `element`
            - `is`
            - `is_not`

### Examples:

#### Validating Title

*Validate the title is "Google"*

```yaml
- validate:
    title: is=Google
```

*Validate the title is **not** "Google"*

```yaml
- validate:
    title: is_not=Google
```

---

#### Validating Text

*Validate the text of an element is "something"*

```yaml
- validate:
    text_of:
      element: css=span.message
      is: something
```

*Validate the text of an element is **not** "something"*

```yaml
- validate:
    text_of:
      element: css=span.message
      is_not: something
```

---

#### Validating Value

*Validate the value attribute of an element is "something"*

```yaml
- validate:
    text_of:
      element: css=span.message
      is: something
```

*Validate the value attribute of an element is **not** "something"*

```yaml
- validate:
    text_of:
      element: css=span.message
      is_not: something
```

---

#### Validating Presence

*Validate that an element is present*

```yaml
- validate:
    present: id=the_id
```

*Validate that an element is not present*

```yaml
- validate:
    not_present: 
      id: the_id
```


