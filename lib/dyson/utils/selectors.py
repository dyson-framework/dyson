from selenium.webdriver.common.by import By
from six import string_types

from dyson.errors import DysonError

ALL_SELECTORS = frozenset(['id', 'name', 'xpath', 'link', 'partiallink', 'tag', 'class', 'css'])


def translate_selector(selector, webdriver):
    """
    Translate the selector into the selenium method to call
    :param selector:
    :param webdriver:
    :return:
    """
    if isinstance(selector, string_types):
        s = selector.split("=", maxsplit=1)
        selector = dict({s[0]: s[1]})  # specifying just a string.  css=something

    if 'id' in selector:
        return getattr(webdriver, 'find_element_by_id'), selector['id']
    elif 'name' in selector:
        return getattr(webdriver, 'find_element_by_name'), selector['name']
    elif 'xpath' in selector:
        return getattr(webdriver, 'find_element_by_xpath'), selector['xpath']
    elif 'link' in selector:
        return getattr(webdriver, 'find_element_by_link_text'), selector['link']
    elif 'partiallink' in selector:
        return getattr(webdriver, 'find_element_by_partial_link_text'), selector['partiallink']
    elif 'tag' in selector:
        return getattr(webdriver, 'find_element_by_tag_name'), selector['tag']
    elif 'class' in selector:
        return getattr(webdriver, 'find_element_by_class_name'), selector['class']
    elif 'css' in selector:
        return getattr(webdriver, 'find_element_by_css_selector'), selector['css']

    return None, None


def is_selector(string: str):
    """
    Check to see if this specific string is a selector
    :param string: the string to check
    :return:
    """
    try:
        sel = string.split("=", maxsplit=1)[0]
        return sel in ALL_SELECTORS
    except:
        return False


def has_selector(string: str):
    """
    Check to see if this specific string contains a selector
    :param string: the string to check
    :return:
    """

    try:
        sel = string.split("=")
        for possible in sel:
            if possible in ALL_SELECTORS:
                return True
        return False
    except:
        return False


def translate_selector_to_by(selector):
    """
    The By class has different ways of selecting things.
    This method translates:
        "css" to By.CSS_SELECTOR
        "name" to By.NAME
        "xpath" to By.XPATH
        "link" to By.LINK_TEXT
        "partiallink" to By.PARTIAL_LINK_TEXT
        "tag" to By.TAG_NAME
        "class" to By.CLASS_NAME

    :param selector: the strategy to check
    :return: the By.* class from Selenium
    """
    valid_selectors = {
        'CSS': 'CSS_SELECTOR',
        'NAME': 'NAME',
        'XPATH': 'XPATH',
        'LINK': 'LINK_TEXT',
        'PARTIALLINK': 'PARTIAL_LINK_TEXT',
        'TAG': 'TAG_NAME',
        'CLASS': 'CLASS_NAME'
    }

    if isinstance(selector, dict):
        the_strategy = next(iter(selector)).upper()
        if the_strategy in valid_selectors:
            return getattr(By, valid_selectors[the_strategy]), next(iter(selector.values()))
        else:
            raise DysonError("%s is not a valid selector. Valid selectors are %s", ','.join(valid_selectors.keys()))

    elif isinstance(selector, string_types):
        the_strategy, the_selector = selector.split("=", maxsplit=1)

        if the_strategy.upper() in valid_selectors:
            return getattr(By, valid_selectors[the_strategy.upper()]), the_selector
        else:
            raise DysonError("%s is not a valid selector. Valid selectors are %s",
                             the_strategy, ','.join([key for key, _ in valid_selectors.items()]))
