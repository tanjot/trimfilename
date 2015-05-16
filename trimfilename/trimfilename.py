#!/usr/bin/python3
import os
import re

from colorama import Fore
from colorama import init
from .utils import PatternLocations
from .utils import renameFile

init(autoreset=True)

class TrimFilename:

    def __init__(self, pattern_position, pattern):
        self.pattern_position = pattern_position
        self.pattern = pattern
        self.renamed_files_list = {}

    def add_to_renamed_list(self, old_name, new_name, dir_path):
        old_path = os.path.join(dir_path, old_name)

        self.renamed_files_list[old_path]=new_name

    def removeDefaultPattern(self, name, dirPath):
        ''' storing name in a list for manipulations on characters individually
        '''
        nameList = list(name)

        #To not rename files starting with only '.'
        if nameList[0] != '.':
            for char in name:
                #remove all non alphabet characters from filename
                if not(char.isalpha() or char == '.'):
                    del(nameList[nameList.index(char)])
                else:
                    break

            new_name = ''.join(nameList)

            if renameFile(name, new_name, dirPath):
                self.add_to_renamed_list(name, new_name, dirPath)

    def removePatternAtBeg(self, name, dirPath, patternToBeRemoved):
        ''' Removes the pattern matched at beginning of the filename
        '''
        new_name = re.sub( '^' +  patternToBeRemoved, '', name)
        if renameFile(name, new_name, dirPath):
            self.add_to_renamed_list(name, new_name, dirPath)

    def removePatternInString(self, name, dirPath, patternToBeRemoved):
        ''' Checks for pattern in whole string and removes it if match is found
        '''
        new_name = re.sub( patternToBeRemoved, '', name )
        if renameFile(name, new_name, dirPath):
            self.add_to_renamed_list(name, new_name, dirPath)

    def removePatternAtEnd(self, name, dirPath, patternToBeRemoved):
        ''' Matches pattern at end of the name
        '''
        new_name = re.sub( patternToBeRemoved + '$', '', name )
        if new_name != name:
            proceedWithRemoval = input("Do you really want to change "
                   "extension from " + name + " to " + new_name + "(y/n) : ")
            #TODO: not prompt for each file
            if(proceedWithRemoval == 'y'):
                if renameFile(name, new_name, dirPath):
                    self.add_to_renamed_list(name, new_name, dirPath)

    def parseDir(self, path):
        ''' Parse the path given for all files and folders contained recursively
        '''
        print('Entered parseDirfname'+path)

        #renamedList contains the list of files renamed
        if os.path.exists(path):
            for dirPath, dirs, files in os.walk(path):

                for name in files:
                    if self.pattern_position == PatternLocations.patternInString:
                        self.removePatternInString(name, dirPath, self.pattern)

                    elif self.pattern_position == PatternLocations.patternAtBeg:
                        self.removePatternAtBeg(name, dirPath, self.pattern)

                    elif self.pattern_position == PatternLocations.patternAtEnd:
                        self.removePatternAtEnd(name, dirPath, self.pattern)

                    else:
                        self.removeDefaultPattern(name, dirPath)

                #Print all directories in current directory
                for name in dirs:
                    fold = os.path.join(dirPath, name)
                    print('Folder: '+fold)

        else:
             print('Path is not valid')

        if self.renamed_files_list:
             print('Files renamed: ')

             str_format = self.get_string_format(self.renamed_files_list.keys())
             for old_path, new_name in self.renamed_files_list.items():
                 print(str_format.format(old_path, ': ' + Fore.RED +   new_name))
             print('Successfully rename '+str(len(self.renamed_files_list))+' file/s')

        else:
            print(Fore.RED + "No file renamed")

    def get_string_format(self, list):
        str_format = '{0:<' + str(len(max(list, key=len))) + '} {1}'
        return str_format