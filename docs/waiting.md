Waiting
=======

*Consider the following `default.yml`*

```yaml
---

element: id=test
title: Title
```

**Note**: 

> Each `wait_for` also allows a customizable timeout. Each `wait_for` defaults to what is set in `dyson.cfg`.
  You can specify a `timeout` key for each. The timeout is in seconds.

---

## Waiting for an element to be present

```yaml
- wait_for:
    presence_of: "element={{ element }}"
```

## Waiting for an element to be visible

```yaml
- wait_for:
    visibility_of: "element={{ element }}"
```

## Waiting for an element to be *in*visible

```yaml
- wait_for:
    invisibility_of: "element={{ element }}"
```

## Waiting for title to be

```yaml
- wait_for:
    title_to_be: "{{ title }}"
```

## Waiting for title to contain

```yaml
- wait_for:
    title_to_contain: "{{ title }}"
```

## Waiting for alert to be present

```yaml
- wait_for:
    alert:
      timeout: "{{ selenium.default_timeout }}"
```

## Waiting for text to be present in element

```yaml
- wait_for:
    text_to_be_present:
      in_element: "{{ element }}"
      text: The Text
```

## Waiting for value to be

```yaml
- wait_for:
    value_to_be:
      in_element: "{{ element }}"
      value: The Value
```

## Waiting for an element to be clickable

```yaml
- wait_for:
    clickable: "element={{ element }}"
```

## Waiting for the staleness of an element

```yaml
- wait_for:
    staleness_of: "element={{ element }}"
```

## Waiting for all elements

```yaml
- wait_for:
    presence_of_all: "elements={{ element }}"
```

## Waiting for element to be selected

```yaml
- wait_for:
    element_to_be_selected: "element={{ element }}"
```

## Waiting for element selection state to be

```yaml
- wait_for:
    selection_state_to_be:
      element: "{{ element }}"
      state: true  # can also be 'yes', 1, or 'True'
```

## Waiting for a frame to be available and switch to it

```yaml
- wait_for:
    frame_and_switch: "frame={{ element }}"
```
