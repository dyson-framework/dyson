import jinja2
from six import string_types

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
            # looking_for = final.split('{{')[1].split('}}')[0].strip()
            t = jinja2.Template(final)
            final = t.render(variable_manager.all)
        if parse_kv:
            final = parse_keyvalue(final)
        return final
    except:
        return val


def iterate_dict(obj, variable_manager, parse_kv=True):
    """
    Iterate through lists and objects and render jinja inside of them
    :param obj: the object
    :param variable_manager:
    :param parse_kv: whether to parse KV.  will be false when going through test vars
    :return:
    """
    new_obj = obj.copy()
    if isinstance(new_obj, dict):
        for item in iter(new_obj):
            if isinstance(new_obj[item], dict):
                new_obj[item] = iterate_dict(new_obj[item], variable_manager=variable_manager, parse_kv=parse_kv)
            elif isinstance(item, string_types):
                new_obj[item] = parse_jinja(new_obj[item], variable_manager=variable_manager, parse_kv=parse_kv)
    elif isinstance(new_obj, list):
        for idx, item0 in enumerate(new_obj):
            if isinstance(new_obj[idx], dict):
                new_obj[idx] = iterate_dict(new_obj[idx], variable_manager=variable_manager, parse_kv=parse_kv)
            elif isinstance(item0, string_types):
                new_obj[idx] = parse_jinja(new_obj[idx], variable_manager=variable_manager, parse_kv=parse_kv)
    return new_obj
