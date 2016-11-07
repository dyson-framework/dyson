import json
import yaml


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
        :param data_loader: the data_loader to load it into
        :return: DataLoader
        """
        try:
            with open(data_file, 'r') as stream:
                the_data = json.loads(stream)
        except:
            # try yaml
            with open(data_file, 'r') as stream:
                the_data = yaml.load(stream)

        return the_data
