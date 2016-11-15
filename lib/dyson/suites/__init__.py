import os

from dyson.tests import Test


class Suite:
    def __init__(self, suite_file, data_loader=None, variable_manager=None, report=None):
        self._suite_file = suite_file
        self._data_loader = data_loader
        self._variable_manager = variable_manager
        self._report = report

    def run(self):
        suite = self._data_loader.load_file(os.path.abspath(self._suite_file))

        for obj in suite:
            if 'tests' in obj:
                for test in obj['tests']:
                    self._report.add_test(
                        Test(os.path.join("tests", test),
                             data_loader=self._data_loader,
                             variable_manager=self._variable_manager).run()
                    )

        self._report.render()
