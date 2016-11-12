import jinja2

from dyson.utils import selectors


def find_all_in(string, whole_string):
    start = 0
    while True:
        start = whole_string.find(string, start)
        if start == -1:
            return
        yield start
        start += len(string)


def parse_keyvalue(arg):
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
            if len(list(find_all_in("=", arg))) > 1:
                for combo in arg.split(" "):
                    (k, v) = combo.split("=", maxsplit=1)
                    all_args[k] = v
            else:
                (k, v) = arg.split("=", maxsplit=1)
                all_args[k] = v
    except ValueError:
        # ignore. it's not a kv combo
        return arg

    return all_args


def parse_jinja(val, variable_manager, parse_kv=True):
    try:
        final = val
        while '{{' in final:
            t = jinja2.Template(final)
            final = t.render(variable_manager.all)
        if parse_kv:
            final = parse_keyvalue(final)
        return final
    except:
        return val
