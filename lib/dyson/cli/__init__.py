from abc import abstractmethod
from optparse import OptionParser

from dyson.reporting import Report


class CLI:
    def __init__(self, args):
        self.args = args
        self.options = None
        self.parser = None
        self._report = Report()

    @staticmethod
    def base_parser(usage="", datafile_opts=False):
        parser = OptionParser(usage, version=CLI.version())
        parser.add_option('-v', '--verbosity', default=0, action="count",
                          help="verbose mode")

        if datafile_opts:
            parser.add_option('-e', '--extra-vars', help="Specify additional variables to override.", action="append",
                              default=[])
            parser.add_option('-a', '--application', help="Specify a particular application to run against.",
                              action="store", default='default.yml')

        return parser

    @abstractmethod
    def parse(self):
        # parse all options, and get the CLI ready to go
        self.options, self.args = self.parser.parse_args(self.args[1:])

        if hasattr(self.options, "tags") and not self.options.tags:
            self.options.tags = ['all']

    @staticmethod
    def version():
        from dyson import __version__ as version
        return version

    @abstractmethod
    def run(self):
        pass

    @property
    def report(self):
        return self._report

    @report.setter
    def report(self, report):
        self._report = report

    @report.getter
    def report(self):
        return self._report

