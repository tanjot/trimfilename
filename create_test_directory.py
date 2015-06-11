#!/usr/bin/python3

import os

def main():
    test_folder = 'test'
    if os.path.isdir(test_folder) is False:
        os.mkdir(test_folder)

    files_to_create = ['123xyz.txt', 'blaabc.blamp3', 'abc.abc']

    for file in files_to_create:
        os.system('touch ' + os.path.join(test_folder, file))


if __name__ == '__main__':
    main()
