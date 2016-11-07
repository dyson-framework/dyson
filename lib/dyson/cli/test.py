import os

from dyson.cli import CLI
from dyson.errors import DysonError
from dyson.utils.dataloader import DataLoader
from dyson.vars import VariableManager, load_extra_vars


class TestCLI(CLI):
    def parse(self):
        self.parser = CLI.base_parser(
            "%prog tests/smoke/steps/main.yml ...",
            datafile_opts=True
        )
        super(TestCLI, self).parse()

    def run(self):
        super(TestCLI, self).run()

        for test in self.args:
            if not os.path.exists(test) or not os.path.isfile(test):
                raise DysonError("Test file %s does not exist" % test)

        dataloader = DataLoader()

        steps = list()

        variablemanager = VariableManager()
        variablemanager.extra_vars = load_extra_vars(loader=dataloader, options=self.options)

        for test in self.args:
            steps.append(dataloader.load_file(test))
            print(steps)

        print(variablemanager.extra_vars)


