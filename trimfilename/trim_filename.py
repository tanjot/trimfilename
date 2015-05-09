#!/usr/bin/python3
import os
import re

from colorama import Fore
from colorama import init
from .utils import PatternLocations

init(autoreset=True)

class TrimFilename:

    def __init__(self, pattern_position, pattern):
        self.pattern_position = pattern_position
        self.pattern = pattern
        self.renamed_file_list = []

    def renameFile(self, oldname, newname, dirPath):
        ''' Renames file if name has changed
        '''
        pathNname = os.path.join(dirPath, oldname)

        #Does not rename file if it begins with '.' or the whole file name gets
        #deleted after rename and also if there is no change in filename
        if newname and newname[0] != '.' and oldname != newname:
            os.rename(pathNname, os.path.join(dirPath, newname))
            #print('Successfully renamed '+pathNname+' to'
            #       ' '+ newname)

            #adding filename to common list of renamed files
            self.renamed_file_list.append(pathNname + ' to ' +  Fore.RED + newname )


       # else:
       #     print('Not renaming, filename : '+pathNname)

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

            self.renameFile(name, ''.join(nameList), dirPath)

    def removePatternAtBeg(self, name, dirPath, patternToBeRemoved):
        ''' Removes the pattern matched at beginning of the filename
        '''
        newname = re.sub( '^' +  patternToBeRemoved, '', name )
        self.renameFile(name, newname, dirPath)

    def removePatternInString(self, name, dirPath, patternToBeRemoved):
        ''' Checks for pattern in whole string and removes it if match is found
        '''
        newname = re.sub( patternToBeRemoved, '', name )
        self.renameFile(name, newname, dirPath)

    def removePatternAtEnd(self, name, dirPath, patternToBeRemoved):
        ''' Matches pattern at end of the name
        '''
        newname = re.sub( patternToBeRemoved + '$', '', name )
        if newname != name:
            proceedWithRemoval = input("Do you really want to change "
                   "extension from "+ name +"(y/n) : ")
            #TODO: not prompt for each file
            if(proceedWithRemoval == 'y'):
                self.renameFile(name, newname, dirPath)


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

        if self.renamed_file_list:
             print('Files renamed: ')
             for name in self.renamed_file_list:
                 print(name)
             print('Successfully rename '+str(len(self.renamed_file_list))+' file/s')
