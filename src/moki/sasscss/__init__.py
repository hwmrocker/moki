import os
import warnings
import tempfile
from subprocess import Popen, PIPE, STDOUT

from django.conf import settings

from compress.filter_base import FilterBase

BINARY = getattr(settings, 'LESSC_BINARY', 'lessc')
ARGUMENTS = getattr(settings, 'LESSC_ARGUMENTS', '>')

warnings.simplefilter('ignore', RuntimeWarning)

class SassCSSFilter(FilterBase):
    def filter_css(self, css):
        p = Popen(['sass', '-s'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        filtered_css = p.communicate(input=css)[0]

        if self.verbose:
            print command_output

        return filtered_css
