Storing Variables
=================

Storing variables, in short, is a way to store variables returned from specific steps
in order to run validations, or perform other actions upon them.

## Examples

```yaml
---
- goto: url=https://google.com
- get_attribute:
    of: name=btnK
    attribute: value
  store: button_value
  
- validate: "'{{ button_value }}' is 'Google Search"
```

```yaml
---
- goto: url=http://localhost:3000
- get_attribute:
    of: css=a[href*='test/']
    attribute: href
  store: the_url
  
- goto: "url={{ the_url }}"
```
