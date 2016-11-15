import ast
import glob
import os
from collections import defaultdict, MutableMapping
from json import dumps

from six import string_types

from dyson.errors import DysonError
from dyson.vars.parsing import parse_keyvalue, iterate_dict


def combine_vars(first_dict, second_dict):
    """
    Return a copy of dictionaries of variables based on configured hash behavior
    """

    return merge_dict(first_dict, second_dict)


def merge_dict(first_dict, second_dict):
    """
    Recursively merges hash b into a so that keys from b take precedence over keys from a
    """

    _validate_mutable_mappings(first_dict, second_dict)

    # if a is empty or equal to b, return b
    if first_dict == {} or first_dict == second_dict:
        return second_dict.copy()

    # if b is empty the below unfolds quickly
    result = first_dict.copy()

    # next, iterate over b keys and values
    for k, v in second_dict.items():
        # if there's already such key in a
        # and that key contains a MutableMapping
        if k in result and isinstance(result[k], MutableMapping) and isinstance(v, MutableMapping):
            # merge those dicts recursively
            result[k] = merge_dict(result[k], v)
        else:
            # otherwise, just copy the value from b to a
            result[k] = v

    return result


def load_extra_vars(loader, options):
    extra_vars = dict()
    for option in options.extra_vars:
        option = str(option)
        if option.startswith(u"@"):
            data = loader.load_from_file(option[1:])
        elif option and option[0] in u'[{':
            data = loader.load(option)
        else:
            # let's try key/value
            data = parse_keyvalue(option)

        extra_vars = combine_vars(extra_vars, data)
    return extra_vars


def load_aut_vars(loader, options, variable_manager):
    aut_vars = dict()
    if options and options.application:
        # first, load in default.yml, then override with $application.yml
        aut_vars = loader.load_file(os.path.abspath(os.path.join(os.path.curdir, "apps", "default.yml")))

        if options.application != "default.yml":
            # don't load default.yml twice.
            aut_vars = merge_dict(aut_vars, loader.load_file(
                os.path.abspath(os.path.join(os.path.curdir, "apps", options.application))))

    return iterate_dict(aut_vars, variable_manager=variable_manager, parse_kv=False)


def load_vars(loader, options, variable_manager):
    variables = dict()

    all_var_files = (
        glob.iglob(os.path.join(os.path.curdir, "vars", "*.yml"), recursive=True),
        glob.iglob(os.path.join(os.path.curdir, "vars", "*.yaml"), recursive=True),
        glob.iglob(os.path.join(os.path.curdir, "vars", "*.json"), recursive=True),
    )

    for possible_var_files in all_var_files:
        for var_files in possible_var_files:
            variables = merge_dict(variables,
                                   loader.load_file(os.path.abspath(var_files)))

    # don't parsekv for variables
    return iterate_dict(variables, variable_manager=variable_manager, parse_kv=False)


def _validate_mutable_mappings(first_hash, second_hash):
    if not (isinstance(first_hash, MutableMapping) and isinstance(second_hash, MutableMapping)):
        myvars = []

        for x in [first_hash, second_hash]:
            try:
                myvars.append(dumps(x))
            except:
                pass
        raise DysonError("Failed to combine dictionaries, expected dicts but got a '{0}' and '{1}': \n{2}\n{3}".format(
            first_hash.__class__.__name__, second_hash.__class__.__name__, myvars[0], myvars[1])
        )


def isidentifier(ident):
    """
    Determines, if string is valid Python identifier using the ast module.
    Orignally posted at: http://stackoverflow.com/a/29586366
    """

    if not isinstance(ident, string_types):
        return False

    try:
        root = ast.parse(ident)
    except SyntaxError:
        return False

    if not isinstance(root, ast.Module):
        return False

    if len(root.body) != 1:
        return False

    if not isinstance(root.body[0], ast.Expr):
        return False

    if not isinstance(root.body[0].value, ast.Name):
        return False

    if root.body[0].value.id != ident:
        return False

    return True


class VariableManager:
    def __init__(self):
        self._extra_vars = defaultdict(dict)
        self._aut_vars = defaultdict(dict)
        self._test_vars = defaultdict(dict)
        self._vars = defaultdict(dict)

        self._additional_vars = defaultdict(dict)

    def add_var(self, var):
        """
        Add an ephemeral variable to use.
        Usually this is used with keyword translations
        :param var: the variable (usually dict)
        :param value: the value
        :return:
        """
        if isinstance(var, list):
            for item in var:
                for obj in item.keys():
                    self._additional_vars[obj] = item[obj]
        elif isinstance(var, dict):
            for obj in var.keys():
                self._additional_vars[obj] = var[obj]

    def clear_additional_vars(self):
        self._additional_vars = defaultdict(dict)

    @property
    def extra_vars(self):
        return self._extra_vars.copy()

    @extra_vars.setter
    def extra_vars(self, value):
        self._extra_vars = value.copy()

    @extra_vars.getter
    def extra_vars(self):
        return self._extra_vars.copy()

    @property
    def aut_vars(self):
        return self._aut_vars.copy()

    @aut_vars.setter
    def aut_vars(self, value):
        self._aut_vars = value.copy()

    @aut_vars.getter
    def aut_vars(self):
        return self._aut_vars.copy()

    @property
    def vars(self):
        return self._vars.copy()

    @vars.setter
    def vars(self, value):
        self._vars = value.copy()

    @vars.getter
    def vars(self):
        return self._vars.copy()

    @property
    def test_vars(self):
        return self._test_vars.copy()

    @test_vars.setter
    def test_vars(self, value):
        if self._test_vars:
            self._test_vars = value.copy()
        else:
            self._test_vars = value

    @test_vars.getter
    def test_vars(self):
        return self._test_vars.copy()

    @property
    def all(self):
        all_vars = dict()

        if self._aut_vars:
            all_vars = self._aut_vars

        if self._aut_vars and self._test_vars:
            all_vars = merge_dict(self._aut_vars, self._test_vars)

        if self._vars:
            all_vars = merge_dict(all_vars, self._vars)

        if self._additional_vars:
            all_vars = merge_dict(all_vars, self._additional_vars)

        from dyson.constants import p
        all_vars = merge_dict(all_vars, p._sections)
        return merge_dict(all_vars, self._extra_vars)

