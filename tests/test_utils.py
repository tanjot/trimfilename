#!/usr/bin/python3

import unittest
import os

from trimfilename.utils import rename_file


class TestRenameFile(unittest.TestCase):

    def test_rename_file_returns_true_if_filename_modified(self):

        oldname='blaa.mp3'
        newname='laa.mp3'
        path='./'
        open(path+oldname, 'w')

        output = rename_file(oldname, newname, path)

        self.assertTrue(output)

        os.remove(path+newname)

