#!/usr/bin/python3

import os


def main():
    test_folder = 'tmp'
    for file_name in get_file_structure():
        create(os.path.join(test_folder, file_name))


def get_file_structure():
    simple_files = ['123xyz.txt', 'fooabc.barmp3', 'abc.abc', '00000000.txt']
    level1_files = ['l1/01-artist-songname.mp3', 'l1/12foo.bar']
    level2_files = ['l1/l2/12.34.56.txt', 'l1/l2/foo.bar']

    files = []
    files.extend(simple_files)
    files.extend(level1_files)
    files.extend(level2_files)
    return files


def create(path):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    touch(path)


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


if __name__ == '__main__':
    main()
