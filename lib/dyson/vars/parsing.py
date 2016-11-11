import jinja2

from dyson.utils import selectors


def parse_keyvalue(arg, has_selector=False):
    """
    Parse options like:
        default_username=Test default_password=TestPassword
    :param arg:
    :return:
    """
    all_args = dict()

    try:
        if selectors.has_selector(arg):
            (k, v) = arg.split("=", maxsplit=1)
            all_args[k] = v
        else:
            for combo in arg.split(" "):
                (k, v) = combo.split("=", maxsplit=1)
                all_args[k] = v
    except ValueError:
        # ignore. it's not a kv combo
        return arg

    return all_args


def parse_jinja(val, variable_manager, parse_kv=True):
    try:
        t = jinja2.Template(val)
        v = t.render(variable_manager.all)
        if parse_kv:
            p = parse_keyvalue(v, has_selector=selectors.has_selector(v))
            return p
        else:
            return v
    except:
        return val
