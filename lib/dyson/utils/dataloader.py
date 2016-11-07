import json
import yaml


class DataLoader:
    def __init__(self):
        self._basedir = '.'

    def load(self, data, file_name='<string>', show_content=True):
        """
        Creates a python data structure from the data which can be
        JSON or YAML
        :param data:
        :param file_name:
        :param show_content:
        :return:
        """
        try:
            the_data = json.loads(data)
        except Exception as e:
            print(e)
            # try yaml
            the_data = yaml.load(data)

        return the_data
