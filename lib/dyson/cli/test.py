import os

from dyson.cli import CLI
from dyson.errors import DysonError
from dyson.utils.dataloader import DataLoader


class TestCLI(CLI):
    def parse(self):
        self.parser = CLI.base_parser(
            "%prog tests/smoke/main.yml ...",
            datafile_opts=True
        )
        super(TestCLI, self).parse()

    def run(self):
        super(TestCLI, self).run()

        for test in self.args:
            if not os.path.exists(test) or not os.path.isfile(test):
                raise DysonError("Test file %s does not exist" % test)

        dataloader = DataLoader()



