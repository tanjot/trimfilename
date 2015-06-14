#!/usr/bin/python3

import unittest
import os

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call

from trimfilename.utils import rename_file

class TestRenameFile(unittest.TestCase):

    @patch('os.rename')
    def test_rename_file_returns_true_if_filename_modified(self, mock_rename):
        mock_rename.return_value = 0
        oldname='123blaa.mp3'
        newname='laa.mp3'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertTrue(output)


    def test_rename_file_returns_false_if_extension_missing(self):
        oldname='blaa.txt'
        newname='blaatxt'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)

    def test_rename_file_returns_false_if_extension_changed(self):
        oldname='blaa.txt'
        newname='blaa.x'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)