import os
from dyson import constants
from abc import abstractmethod

import sys

from dyson.constants import to_boolean


class DysonModule:
    def __init__(self):
        pass

    @abstractmethod
    def run(self, webdriver, params):
        pass

    def fail(self, msg):
        print(msg, file=sys.stderr)
        if not to_boolean(constants.DEFAULT_SELENIUM_PERSIST):
            exit(2)


def get_module_path():
    return os.path.dirname(os.path.realpath(__file__))
