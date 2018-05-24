#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":

    this = os.path.basename(sys.argv[0])
    cli = None

    # this will be populated by file checking in the future
    dyson_submodule = sys.argv[1]

    # if this.find('-') != -1:
        # target_cli = this.split('-')[1]
    if (dyson_submodule):
        theclass = "%sCLI" % dyson_submodule.capitalize()
        the_cli = getattr(__import__("dyson.cli.%s" % dyson_submodule, fromlist=[theclass]), theclass)
    else:
        from dyson.cli import AdHocCLI as the_cli

    args = sys.argv[1:]

    cli = the_cli(args)
    cli.parse()
    rc = cli.run()
    exit(rc)
