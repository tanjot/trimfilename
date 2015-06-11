#!/usr/bin/python3

import os


def main():
    test_folder = 'tmp'
    files_to_create = ['123xyz.txt', 'blaabc.blamp3', 'abc.abc']

    for file in files_to_create:
        create(os.path.join(test_folder, file))


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
