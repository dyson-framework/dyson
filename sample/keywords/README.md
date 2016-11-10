Framework-wide Keywords
=======================

Here you can put any keywords.

Keywords are files that act like modules, but execute individual steps.

An example keyword, would be:

```yaml
---

- wait_for: "visibility_of={{ my_click }}"
- click: "{{ my_click }}"

```

You could then save the above keyword as "my_click.yml" and you can call "- my_click: css=something" to wait for
the element before clicking.
