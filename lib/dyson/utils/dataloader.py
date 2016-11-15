import json

import yaml
from six import string_types

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

    def load_file(self, data_file):
        """
        Loads a JSON/YAML file
        :param data_file: the file to load
        :return: DataLoader
        """
        datum = None

        try:
            with open(data_file, 'r') as stream:
                the_data = json.loads(stream)
        except:
            with open(data_file, 'r') as stream:
                the_data = yaml.load(stream)

        return the_data
