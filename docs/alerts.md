Alerts
======

To handle alerts in Dyson, you can use the `switch_to` module.

## Switch to alert and Dismiss

```yaml
- switch_to:
    alert: action=dismiss
```

## Switch to alert and Accept

```yaml
- switch_to:
    alert: action=accept
```

## Switch to alert and Authenticate

```yaml
- switch_to:
    alert: username=the_username password=the_password
```

## Switch to alert and get the text

```yaml
- switch_to:
    alert: action=get_text
  register: alert_text
  
- validate: "{{ alert_text }} is 'The alert text'"
```
