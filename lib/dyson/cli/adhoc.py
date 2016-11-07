from dyson.cli import CLI


class AdHocCLI(CLI):
    def parse(self):
        self.parser = CLI.base_parser(
            "%prog --help"
        )

        super(AdHocCLI, self).parse()

    def run(self):
        super(AdHocCLI, self).run()
