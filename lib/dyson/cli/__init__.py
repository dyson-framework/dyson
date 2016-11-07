from abc import abstractmethod
from optparse import OptionParser


class CLI:
    def __init__(self, args, callback=None):
        self.args = args
        self.options = None
        self.parser = None
        self.callback = callback

    @staticmethod
    def base_parser(usage="", datafile_opts=False):
        parser = OptionParser(usage, version=CLI.version())
        parser.add_option('-v', '--verbosity', default=0, action="count",
                          help="verbose mode")

        if datafile_opts:
            parser.add_option('-d', '--data-file', help="Specify a data file for dyson to use.")

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
        print("running")

