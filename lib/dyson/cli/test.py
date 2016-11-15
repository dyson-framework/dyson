import os

from dyson.cli import CLI
from dyson.errors import DysonError
from dyson.tests import Test
from dyson.utils.dataloader import DataLoader
from dyson.vars import VariableManager, load_extra_vars, load_aut_vars, load_vars


class TestCLI(CLI):
    def parse(self):
        self.parser = CLI.base_parser(
            "%prog tests/smoke/steps/main.yml ...",
            datafile_opts=True
        )
        self.parser.add_option('-b', '--browser', help="Specify which browser to run. e.g. chrome, firefox")
        super(TestCLI, self).parse()

    def run(self):
        super(TestCLI, self).run()

        for test in self.args:
            if not os.path.exists(test):
                raise DysonError("Test file %s does not exist" % test)

        dataloader = DataLoader()

        variablemanager = VariableManager()
        variablemanager.extra_vars = load_extra_vars(loader=dataloader, options=self.options)
        variablemanager.aut_vars = load_aut_vars(loader=dataloader, options=self.options,
                                                 variable_manager=variablemanager)
        variablemanager.vars = load_vars(loader=dataloader, options=self.options,
                                         variable_manager=variablemanager)

        for test in self.args:
            self.report.add_test(Test(test, data_loader=dataloader, variable_manager=variablemanager).run())
            self.report.render()



