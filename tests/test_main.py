#!/usr/bin/env python

from __future__ import print_function

import os
import sys

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call

from trimfilename.main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.folder_name = 'tmp'
        self.argv_backup = sys.argv

    def tearDown(self):
        sys.argv = self.argv_backup

    @patch('trimfilename.main.TrimFilename.parseDir')
    def test_should_parse_folder_if_available_with_short_flag(self,
                                                              mock_parse_dir):
        mock_parse_dir.return_value = 0
        sys.argv = ['dummy', '-f', self.folder_name]
        main()
        mock_parse_dir.assert_called_once_with(self.folder_name)

    @patch('trimfilename.main.TrimFilename.parseDir')
    def test_should_parse_folder_if_available_with_long_flag(self,
                                                             mock_parse_dir):
        mock_parse_dir.return_value = 0
        sys.argv = ['dummy', '--folder', self.folder_name]
        main()
        mock_parse_dir.assert_called_once_with(self.folder_name)

    @patch('trimfilename.main.TrimFilename.parseDir')
    def test_should_parse_cwd_if_no_arguments_passed(self, mock_parse_dir):
        mock_parse_dir.return_value = 0
        sys.argv = ['dummy']
        main()
        mock_parse_dir.assert_called_once_with(os.getcwd())


class AnyStringContaining(str):
    def __eq__(self, other):
        return self in other


if __name__ == '__main__':
    unittest.main()
