import os

from dyson.tests import Test


class Suite:
    def __init__(self, suite_file, data_loader=None, variable_manager=None):
        self._suite_file = suite_file
        self._data_loader = data_loader
        self._variable_manager = variable_manager

    def run(self):
        suite = self._data_loader.load_file(os.path.abspath(self._suite_file))

        for obj in suite:
            if 'tests' in obj:
                for test in obj['tests']:
                    Test(os.path.join("tests", test),
                         data_loader=self._data_loader,
                         variable_manager=self._variable_manager).run()
