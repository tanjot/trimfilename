#!/usr/bin/python3
import os
import re

from colorama import Fore
from colorama import init
from .utils import PatternLocations
from .utils import rename_file

init(autoreset=True)


class TrimFilename:
    def __init__(self, pattern_position, pattern, ignore_case):
        self.pattern_position = pattern_position
        self.pattern = pattern
        self.renamed_files_list = {}
        self.ignore_case = ignore_case

    def add_to_renamed_list(self, old_name, new_name, dir_path):
        old_path = os.path.join(dir_path, old_name)

        self.renamed_files_list[old_path] = new_name

    def remove_default_pattern(self, name, dirPath):
        """ storing name in a list for manipulations on characters individually
        """
        nameList = list(name)

        # To not rename files starting with only '.'
        if nameList[0] != '.':
            for char in name:
                # remove all non alphabet characters from filename
                if char.isalpha() is False:
                    del (nameList[nameList.index(char)])
                elif char == '.' and (''.join(nameList).count('.')) > 1:
                    del (nameList[nameList.index(char)])
                else:
                    break

            new_name = ''.join(nameList)

            if rename_file(name, new_name, dirPath):
                self.add_to_renamed_list(name, new_name, dirPath)

    def remove_pattern_at_beg(self, name, dirPath, patternToBeRemoved):
        """ Removes the pattern matched at beginning of the filename
        """
        if self.ignore_case:
            new_name = re.sub('^' + patternToBeRemoved, '', name,
                              flags=re.IGNORECASE)
        else:
            new_name = re.sub('^' + patternToBeRemoved, '', name)

        if rename_file(name, new_name, dirPath):
            self.add_to_renamed_list(name, new_name, dirPath)

    def remove_pattern_in_string(self, name, dirPath, patternToBeRemoved):
        """ Checks for pattern in whole string and removes it if match is found
        """
        if self.ignore_case:
            new_name = re.sub(patternToBeRemoved, '', name,
                              flags=re.IGNORECASE)
        else:
            new_name = re.sub(patternToBeRemoved, '', name)

        if rename_file(name, new_name, dirPath):
            self.add_to_renamed_list(name, new_name, dirPath)

    def remove_pattern_at_end(self, name, dirPath, patternToBeRemoved):
        """ Matches pattern at end of the name
        """
        if self.ignore_case:
            new_name = re.sub(patternToBeRemoved + '$', '', name,
                              flags=re.IGNORECASE)
        else:
            new_name = re.sub(patternToBeRemoved + '$', '', name)

        if new_name != name:
            proceedWithRemoval = input(
                "Do you really want to change "
                "extension from " + name + " to " + new_name + "(y/n) : ")
            # TODO: not prompt for each file
            if (proceedWithRemoval == 'y'):
                if rename_file(name, new_name, dirPath):
                    self.add_to_renamed_list(name, new_name, dirPath)

    def parseDir(self, path):
        ''' Parse the path given for all files and folders contained recursively
        '''

        # renamedList contains the list of files renamed
        if os.path.exists(path):
            for dirPath, dirs, files in os.walk(path):

                for name in files:
                    if self.pattern_position == PatternLocations.patternInString:
                        self.remove_pattern_in_string(name, dirPath,
                                                      self.pattern)

                    elif self.pattern_position == PatternLocations.patternAtBeg:
                        self.remove_pattern_at_beg(name, dirPath, self.pattern)

                    elif self.pattern_position == PatternLocations.patternAtEnd:
                        self.remove_pattern_at_end(name, dirPath, self.pattern)

                    else:
                        self.remove_default_pattern(name, dirPath)

                # Print all directories in current directory
                for name in dirs:
                    fold = os.path.join(dirPath, name)
                    print('Folder: ' + fold)

        else:
            print('Path is not valid')

        if self.renamed_files_list:
            print('Files renamed: ')

            str_format = self.get_string_format(self.renamed_files_list.keys())
            for old_path, new_name in self.renamed_files_list.items():
                print(str_format.format(old_path, ': ' + Fore.RED + new_name))
            print('Successfully rename ' + str(len(self.renamed_files_list)) +
                  ' file/s')

        else:
            print(Fore.RED + "No file renamed")

    def get_string_format(self, list):
        str_format = '{0:<' + str(len(max(list, key=len))) + '} {1}'
        return str_format
