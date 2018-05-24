import os

from dyson.cli import CLI
from dyson.errors import DysonError
from dyson.suites import Suite
from dyson.utils.dataloader import DataLoader
from dyson.vars import VariableManager, load_extra_vars, load_aut_vars, load_vars


class SuiteCLI(CLI):
    def parse(self):
        self.parser = CLI.base_parser(
            "%prog suite.yml ...",
            datafile_opts=True
        )
        self.parser.add_option('-b', '--browser', help="Specify which browser to run. e.g. chrome, firefox")
        self.parser.add_option('-d', '--base-dir', help="Sets the base directory to run the app")
        super(SuiteCLI, self).parse()

    def run(self):
        super(SuiteCLI, self).run()

        for suite in self.args:
            if not os.path.exists(suite):
                raise DysonError("Suite file %s does not exist" % suite)

        dataloader = DataLoader({"basedir": self.options.base_dir})

        # initialize constants using base_dir
        from dyson import constants
        constants.init({"basedir": self.options.base_dir})

        variablemanager = VariableManager()
        variablemanager.extra_vars = load_extra_vars(loader=dataloader, options=self.options)
        variablemanager.aut_vars = load_aut_vars(loader=dataloader, options=self.options,
                                                 variable_manager=variablemanager)
        variablemanager.vars = load_vars(loader=dataloader, options=self.options,
                                         variable_manager=variablemanager)

        for suite in self.args:
            Suite(suite, data_loader=dataloader, variable_manager=variablemanager, report=self.report).run()
