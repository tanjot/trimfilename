#!/usr/bin/python3

import unittest
import pathlib
import os

from trimfilename.utils import rename_file
from pathlib import PurePath, Path

from unittest.mock import patch

@patch ('trimfilename.utils.rename_file')
class TestRenameFile(unittest.TestCase):

    def test_rename_file_returns_true_for_renamed_file(self, mock_rename_file):

        oldname='blaa.mp3'
        newname='laa.mp3'
        path='./'
        open(path+oldname, 'w')

        output = rename_file(oldname, newname, path)

        self.assertTrue(output)

        os.remove(path+newname)
