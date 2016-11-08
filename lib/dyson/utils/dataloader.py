import json

import yaml
from six import string_types

from dyson.vars import isidentifier
from dyson.vars.parsing import parse_jinja


class DataLoader:
    def __init__(self):
        self._basedir = '.'

    def load(self, data):
        """
        Creates a python data structure from the data which can be
        JSON or YAML
        :param data:
        :return:
        """
        try:
            the_data = json.loads(data)
        except:
            # try yaml
            the_data = yaml.load(data)

        return the_data

    def load_file(self, data_file, variable_manager=None):
        """
        Loads a JSON/YAML file
        :param data_file: the file to load
        :param variable_manager:
        :return: DataLoader
        """
        datum = None

        try:
            with open(data_file, 'r') as stream:
                the_data = json.loads(stream)
        except:
            # try yaml
            with open(data_file, 'r') as stream:
                the_data = yaml.load(stream)

        if variable_manager and the_data:
            datum = self._iterate(the_data, variable_manager)

        if datum:
            return datum
        else:
            return the_data

    def _iterate(self, obj, variable_manager):
        """
        Iterate through lists and objects and render jinja inside of them
        :param obj: the object
        :param variable_manager: the variable manager
        :return:
        """
        new_obj = obj.copy()
        if isinstance(new_obj, dict):
            for item in iter(new_obj):
                if isinstance(new_obj[item], dict):
                    new_obj[item] = self._iterate(new_obj[item], variable_manager)
                elif isinstance(item, string_types):
                    new_obj[item] = parse_jinja(new_obj[item], variable_manager)
        elif isinstance(new_obj, list):
            for idx, item0 in enumerate(new_obj):
                if isinstance(new_obj[idx], dict):
                    new_obj[idx] = self._iterate(new_obj[idx], variable_manager)
                elif isidentifier(item0):
                    new_obj[idx] = parse_jinja(new_obj[idx], variable_manager)
        return new_obj
