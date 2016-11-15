Cookies
=======

In the [Extra Modules](https://github.com/dynamictivity/dyson-modules-extras) 
repository, there exist some modules for you to deal with cookies.

## Add Cookies

```yaml
---
- add_cookies:
    - name: var1
      value: something
      path: /
    - name: var2
      value: something else
      httpOnly: true
```

As you can see from the command above, we are able to specify any configuration
of cookie we want.

## Get Cookies

```yaml
---

# get one cookie
- get_cookies: name=var1
  store: my_cookie
  
- validate: "'{{ my_cookie['value'] }}' is 'something'"

# get multiple cookies
- get_cookies:
    - my_cookie1
    - my_cookie2
  store: my_cookies
  
# get all cookies
- get_cookies: all
  store: all_cookies
```

When getting cookies, Dyson will return the `org.openqa.selenium.Cookie` object

The object returns something like this:

`{'class': 'org.openqa.selenium.Cookie', 'value': 'test', 'secure': False, 'hCode': -1958641577, 'domain': 'www.google.com', 'name': 'my_cookie', 'httpOnly': False, 'path': '/'}`

In order to access the variables, you can use bracket notation on the object.

`my_cookie['value']` to return `test`
