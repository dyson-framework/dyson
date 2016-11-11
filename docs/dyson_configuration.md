Dyson Configuration
===================

- [Definition](#definition)
- [Configuration File](#configuration-file)

Dyson has the following configurations

- [http](#http)
  * [protocol](#protocol) - *default: http*
  * [user_agent](#user-agent) - *default: &lt;whatever browser you are using&gt;*
- [timeouts](#timeouts)
  * [default_timeout](#default-timeout) - *default: '5'. in seconds*
- [selenium](#selenium)
  * [browser](#browser)
  * [hub](#hub) - *default: http://127.0.0.1:4444/wd/hub*
  * [implicit_wait](#implicit-wait) - *default: 10*
  * [persist](#persistance-mode) - *default: yes*
  
---

# Definition

## HTTP

All HTTP specific variables

### Protocol

The HTTP Protocol to use. Dyson defaults this to 'http', but you may also
 specify 'https'
 
### User Agent

This tells Selenium which user agent to use.  By default, this will be
whatever browser you are using.  If you have applications that only work
with specific versions, you are able to tell Selenium that you are using
a different user agent

---

## Timeouts

All timeout related variables

### Default Timeout

With every [`wait_for`](https://github.com/dynamictivity/dyson/tree/master/docs/waiting.md),
Dyson will read this value and pass it into the `wait_for` steps by default.

Timeouts are in **seconds**

---

## Selenium

All Selenium related settings

### Browser

This tells Dyson which browser to use.  This can be any browser [set here](https://github.com/SeleniumHQ/selenium/blob/master/py/selenium/webdriver/common/desired_capabilities.py#L50)

### Implicit Wait

> "An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available" - [Selenium](https://selenium-python.readthedocs.io/waits.html#implicit-waits)

This value defaults to `0`

### Persistance Mode

Persistance mode is whether or not to continue upon test failure.

By setting persistance to false, Dyson will stop upon test failure.

This defaults to **true**, but can be set to `no`,`false`, `0`

---

# Configuration File

Dyson requires that a `dyson.cfg` file exists in your project root.

You can see an example in Dyson's [Sample dyson.cfg file](https://github.com/dynamictivity/dyson/tree/master/sample/dyson.cfg)
