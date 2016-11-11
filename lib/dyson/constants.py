import os

from six import string_types

from dyson.errors import DysonError
import configparser

from dyson.utils.quotes import unquote

BOOL_TRUE = frozenset(["true", "t", "y", "1", "yes", "on"])


def shell_expand(path, expand_relative_paths=False):
    if path:
        path = os.path.expanduser(os.path.expandvars(path))
        if expand_relative_paths and not path.startswith('/'):
            if 'CONFIG_FILE' in globals():
                CFGDIR = os.path.dirname(CONFIG_FILE)
                path = os.path.join(CFGDIR, path)
            path = os.path.abspath(path)
    return path


def load_config_file():
    """ Load Config File order (first found is used).  environment variable, working dir, HOME """

    p = configparser.ConfigParser()

    path0 = os.getenv("DYSON_CONFIG", None)
    if path0 is not None:
        path0 = os.path.expanduser(path0)
        if os.path.isdir(path0):
            path0 += "/dyson.cfg"
    try:
        path1 = os.getcwd() + "/dyson.cfg"
    except OSError:
        path1 = None
    path2 = os.path.expanduser("~/.dyson.cfg")

    for path in [path0, path1, path2]:
        if path is not None and os.path.exists(path):
            try:
                p.read(path)
            except configparser.Error as e:
                raise DysonError("Error reading config file: \n{0}".format(e))
            return p, path
    return None, ''


def to_boolean(value):
    if value is None:
        return False
    val = str(value)
    return val.lower() in BOOL_TRUE


def get_config(p, section, key, env_var, default, value_type=None, expand_relative_paths=False):
    value = _get_config(p, section, key, env_var, default)

    if value_type == 'boolean':
        value = to_boolean(value)

    elif value:
        if value_type == 'integer':
            value = int(value)

        elif value_type == 'float':
            value = float(value)

        elif value_type == 'list':
            if isinstance(value, string_types):
                value = [x.strip() for x in value.split(',')]

        elif value_type == 'none':
            if value == "None":
                value = None

        elif value_type == 'path':
            value = shell_expand(value)

        elif value_type == 'pathlist':
            if isinstance(value, string_types):
                value = [shell_expand(x, expand_relative_paths=expand_relative_paths)
                         for x in value.split(os.pathsep)]

        elif isinstance(value, string_types):
            value = unquote(value)

    return str(value)


def _get_config(p, section, key, env_var, default):
    if env_var is not None:
        value = os.environ.get(env_var, None)
        if value is not None:
            return value
    if p is not None:
        try:
            return p.get(section, key, raw=True)
        except:
            return default
    return default


p, CONFIG_FILE = load_config_file()

DEFAULTS = 'defaults'
HTTP = 'http'
TIMEOUTS = 'timeouts'
SELENIUM = 'selenium'

DEFAULT_DEBUG = get_config(p, DEFAULTS, 'debug', 'DYSON_DEBUG', False, value_type='boolean')

# http settings
DEFAULT_HTTP_PROTOCOL = get_config(p, HTTP, 'protocol', 'DYSON_HTTP_PROTOCOL', 'http', value_type='string')
DEFAULT_HTTP_USER_AGENT = get_config(p, HTTP, 'user_agent', 'DYSON_HTTP_USER_AGENT', None, value_type='string')

# selenium settings
DEFAULT_SELENIUM_HUB = get_config(p, SELENIUM, 'hub', 'DYSON_SELENIUM_HUB', 'http://127.0.0.1:4444/wd/hub',
                                  value_type='string')
DEFAULT_SELENIUM_BROWSER = get_config(p, SELENIUM, 'browser', 'DYSON_SELENIUM_BROWSER', None, value_type='string')
DEFAULT_SELENIUM_PERSIST = get_config(p, SELENIUM, 'persist', 'DYSON_SELENIUM_PERSIST', True, value_type='boolean')
DEFAULT_SELENIUM_IMPLICIT_WAIT = get_config(p, SELENIUM, 'implicit_wait', 'DYSON_SELENIUM_IMPLICIT_WAIT', 0,
                                            value_type='int')

# timeout settings
DEFAULT_TIMEOUT = get_config(p, TIMEOUTS, 'default_timeout', 'DYSON_DEFAULT_TIMEOUT', 5, value_type='int')
