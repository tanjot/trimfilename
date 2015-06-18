#!/usr/bin/python3

import os

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


class TestAddToRenamedList(unittest.TestCase):

    def setUp(self):
        self.tfn_handle = TrimFilename(None, None, None)
        # self.tfn_handle.renamed_list = [ '123abc.txt':'abc.txt', '0913903bla.txt':'bla.txt']

    def test_add_to_renamed_list_when_list_is_empty(self):
        oldname = '233xyz.txt'
        newname = 'xyz.txt'
        path='.'

        renamed_list = {os.path.join(path, oldname):newname}
        self.tfn_handle.add_to_renamed_list(oldname, newname, path)

        self.assertEqual(renamed_list,self.tfn_handle.renamed_files_list)

