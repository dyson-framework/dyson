import glob
import os
import pathlib

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from dyson.errors import DysonError
from dyson.keywords import load_keywords
from dyson.modules import load_modules
from dyson.steps import Step
from dyson.utils.dataloader import DataLoader
from dyson.vars import merge_dict
from dyson.vars.parsing import iterate_dict


class Test:
    def __init__(self, test_file, data_loader=None, variable_manager=None):
        self._test_file = test_file
        self._data_loader = data_loader
        self._variable_manager = variable_manager
        self._webdriver = webdriver
        self._steps = list()

        if os.path.isdir(os.path.expanduser(test_file)):
            self._test_file = self._resolve_main()

        self._test_path = self._resolve_base_path()
        self._modules = load_modules(self._test_path)
        self._keywords = load_keywords(self._test_path)

        self._variable_manager.test_vars = self._resolve_test_vars()

    def run(self):
        # first let's get the steps
        all_steps = self._data_loader.load_file(self._test_file)

        # iterate through all includes
        all_steps = self._resolve_all_includes(all_steps)

        self._start_selenium()

        try:
            for step in all_steps:
                # run each step

                step = iterate_dict(step, variable_manager=self._variable_manager)

                if 'store' in step:
                    var_name = step['store']
                    del step['store']

                    _, _, retval = Step(step,
                                        data_loader=self._data_loader,
                                        variable_manager=self._variable_manager,
                                        modules=self._modules,
                                        webdriver=self._webdriver, keywords=self._keywords).run()
                    self._variable_manager.add_var({var_name: retval})
                else:
                    Step(step,
                         data_loader=self._data_loader,
                         variable_manager=self._variable_manager,
                         modules=self._modules,
                         webdriver=self._webdriver, keywords=self._keywords).run()
        finally:
            self._webdriver.quit()

        return os.path.basename(self._test_file), all_steps

    def _resolve_main(self):
        # only applies when user is specifying a directory.
        # need to poll through the test directory
        allowed_mains = (
            os.path.expanduser(os.path.join(self._test_file, "steps", "main.yml")),
            os.path.expanduser(os.path.join(self._test_file, "steps", "main.yaml")),
            os.path.expanduser(os.path.join(self._test_file, "steps", "main.json")),
        )

        number_of_mains = 0
        for allowed_main in allowed_mains:
            if os.path.exists(allowed_main) and os.path.isfile(allowed_main):
                main_file = allowed_main
                number_of_mains += 1

        if number_of_mains > 1:
            raise DysonError("There are more than one main files in %s. Only one is allowed")
        elif number_of_mains == 0:
            raise DysonError("There are no steps to run in directory %s.  A main file must exist" % self._test_file)
        else:
            return main_file

    def _resolve_include(self, included_file, data_loader: DataLoader):
        file_to_include = os.path.expanduser(os.path.join(self._test_path, "steps", "%s" % included_file))
        new_step = data_loader.load_file(file_to_include)
        return new_step

    def _resolve_all_includes(self, all_steps):
        for idx, step in enumerate(all_steps):
            # first, resolve all includes and put them into the dict
            if 'include' in step.keys():
                del all_steps[idx]
                for s in self._resolve_include(step['include'], data_loader=self._data_loader):
                    all_steps.append(s)
        for step in all_steps:
            if 'include' in step.keys():
                all_steps = self._resolve_all_includes(all_steps)
            else:
                return all_steps

    def _resolve_base_path(self):
        """
        Resolve the base path of this specific test file.
        Step files always reside in steps/main.yml, so we
        need to up two directories.
        :return:
        """
        return str(pathlib.Path(os.path.abspath(self._test_file)).parents[1])

    def _resolve_test_vars(self):
        test_vars = dict()

        vars_files = (
            glob.iglob(os.path.join(self._test_path, "vars", "*.yml"),  recursive=True),
            glob.iglob(os.path.join(self._test_path, "vars", "*.yaml"), recursive=True),
            glob.iglob(os.path.join(self._test_path, "vars", "*.json"), recursive=True),
        )

        for possible_var_files in vars_files:
            for vars_file in possible_var_files:
                if os.path.exists(vars_file):
                    test_vars = merge_dict(test_vars,
                                           self._data_loader.load_file(vars_file))

        return iterate_dict(test_vars, variable_manager=self._variable_manager, parse_kv=False)

    def _start_selenium(self):
        from dyson import constants
        browser = constants.DEFAULT_SELENIUM_BROWSER.capitalize()
        if hasattr(self._webdriver, browser) and hasattr(DesiredCapabilities, browser.upper()):
            command_executor = constants.DEFAULT_SELENIUM_HUB
            if command_executor:
                self._webdriver = self._webdriver.Remote(
                    command_executor=command_executor,
                    desired_capabilities=getattr(DesiredCapabilities, browser.upper())
                )
                self._webdriver.implicitly_wait(constants.DEFAULT_SELENIUM_IMPLICIT_WAIT)
            else:
                self._webdriver = getattr(self._webdriver, browser)()
        else:
            raise DysonError("Invalid browser " % constants.DEFAULT_SELENIUM_BROWSER)

