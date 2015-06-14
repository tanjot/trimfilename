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

@patch('os.rename')
class TestRenameFile(unittest.TestCase):

    def test_rename_file_returns_true_if_filename_modified(self, mock_rename):
        mock_rename.return_value=True
        oldname='123blaa.mp3'
        newname='laa.mp3'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertTrue(output)

    def test_rename_file_returns_false_if_extension_missing(self, mock_rename):
        mock_rename.return_value=True
        oldname='blaa.txt'
        newname='blaatxt'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)

    def test_rename_file_returns_false_if_extension_changed(self, mock_rename):
        mock_rename.return_value=True
        oldname='blaa.txt'
        newname='blaa.x'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)

    def test_rename_file_returns_false_if_newname_starts_with_dot(self, mock_rename):
        mock_rename.return_value=True
        oldname='132.txt'
        newname='.txt'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)


    def test_rename_file_returns_false_if_oldname_newname_are_same(self, mock_rename):
        mock_rename.return_value=True
        oldname='132blaa.txt'
        newname='132blaa.txt'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)


    def test_rename_file_returns_false_if_newname_is_empty(self, mock_rename):
        mock_rename.return_value=True
        oldname='123'
        newname=''
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)

    def test_rename_file_if_extension_removed(self, mock_rename):
        mock_rename.return_value=True
        oldname='123.45.abc.txt'
        newname='123.45.abc.'
        path='./'

        output = rename_file(oldname, newname, path)

        self.assertFalse(output)
