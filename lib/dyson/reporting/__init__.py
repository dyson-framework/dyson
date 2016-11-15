import datetime
import os
import time

import jinja2

from dyson.tests import Test


class Report:
    def __init__(self):
        self._tests = list()

    def render(self):
        """
        Render a report
        :return:
        """

        template = """
        <html>Hi there</html>
        """
        # first let's find the report j2 template
        if os.path.exists(os.path.join(os.path.curdir, "reports", "default.j2")):
            f = open(os.path.join(os.path.curdir, "reports", "default.j2"))
            template = f.read()

        report_name = "%s-%s.txt"

        # TODO: Finish reporting

        # for test, steps in self._tests:
        #     timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
        #     print(test)
        #     with open(report_name % (test, timestamp), 'w') as report:
        #         t = jinja2.Template(template)
        #         v = t.render({'steps': steps[0], 'test_name': test})
        #         report.write(v)

    def add_test(self, test: Test):
        """
        Add a test that was run, to the report
        :param test:
        :return:
        """
        self._tests.append(test)
