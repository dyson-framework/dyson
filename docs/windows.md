Dealing with Windows
====================

In the [Core Modules](https://github.com/dynamictivity/dyson-modules-core),
there exist a couple modules for you to deal with windows and 
switching between them.

## Switching to a Window

```yaml
---

- get_window_handles:
  store: window_handles

- switch_to:
    window: "{{ window_handles[1] }}"
```

A couple notes.  First, we are [storing a variable](https://github.com/dynamictivity/dyson/tree/master/docs/storing_variables.md)
to the value of all window handles.  Since this module in specific
returns the python object of `driver.window_handles`,
we are able to operate upon it just as you would in python.

We are switching to the second opened window (since these indices are zero-based)

