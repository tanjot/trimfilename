#!/usr/bin/python3

from trimfilename.trimfilename import TrimFilename

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call

class TestGetStringFormat(unittest.TestCase):

    def setUp(self):
        self.tfn_handle = TrimFilename(None, None, None)

    def test_get_string_format_returns_correct_output(self):

        list = ['apple', 'samsung', 'motorola', 'ericsson']
        expected_format = '{0:<' + str(len(max(list, key=len))) + '} {1}'

        self.assertEquals(expected_format, self.tfn_handle.get_string_format(list))

