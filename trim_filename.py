#!/usr/bin/python3
import sys
import os
import re
import argparse
from colorama import Fore
from colorama import init

init(autoreset=True)

#define function main
def main(arg = sys.argv):

    #initializing argument parser
    parser = argparse.ArgumentParser()

    #adding arguments
    parser.add_argument("path", help="Give the path name to rename files",
            type=str, nargs='+')
    parser.add_argument("-p", "--patternInString", help="Give the pattern that is to "
                "be removed", type=str)
    parser.add_argument("-pb", "--patternAtBeg", help="Pattern to be removed "
                "is matched at beginning of the filenames", type=str)
    parser.add_argument("-pe", "--patternAtEnd", help="Pattern to be removed "
                "is matched at end of the filenames(extension should be "
                "included in pattern)", type=str)


    #parsing arguments
    argu = parser.parse_args()

    #TODO: not pass argu as parameter
    for name in argu.path:
        print(name)
        parseDir(name,argu)

def renameFile(oldname, newname, dirPath, renamedList):
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
        renamedList.append(pathNname + ' to ' +  Fore.RED + newname )


   # else:
   #     print('Not renaming, filename : '+pathNname)

def removeDefaultPattern(name, dirPath, renamedList):
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

        renameFile(name, ''.join(nameList), dirPath, renamedList)

def removePatternAtBeg(name, dirPath, patternToBeRemoved, renamedList):
    ''' Removes the pattern matched at beginning of the filename
    '''
    newname = re.sub( '^' +  patternToBeRemoved, '', name )
    renameFile(name, newname, dirPath, renamedList)

def removePatternInString(name, dirPath, patternToBeRemoved, renamedList):
    ''' Checks for pattern in whole string and removes it if match is found
    '''
    newname = re.sub( patternToBeRemoved, '', name )
    renameFile(name, newname, dirPath, renamedList)

def removePatternAtEnd(name, dirPath, patternToBeRemoved, renamedList):
    ''' Matches pattern at end of the name
    '''
    newname = re.sub( patternToBeRemoved + '$', '', name )
    if newname != name:
        proceedWithRemoval = input("Do you really want to change "
               "extension from "+ name +"(y/n) : ")
        #TODO: not prompt for each file
        if(proceedWithRemoval == 'y'):
            renameFile(name, newname, dirPath, renamedList)


def parseDir(fname, argu):
    ''' Parse the path given for all files and folders contained recursively
    '''
    print('Entered parseDirfname'+fname)

    #renamedList contains the list of files renamed
    renamedList = []
    if os.path.exists(fname):
        for dirPath, dirs, files in os.walk(fname):

            for name in files:
                if argu.patternInString:
                    patternToBeRemoved = argu.patternInString
                    match = re.search(patternToBeRemoved+'\w+', name)
                    removePatternInString(name, dirPath, patternToBeRemoved,
                            renamedList)
                elif argu.patternAtBeg:
                    patternToBeRemoved = argu.patternAtBeg
                    removePatternAtBeg(name, dirPath, patternToBeRemoved,
                                renamedList)

                elif argu.patternAtEnd:
                    patternToBeRemoved = argu.patternAtEnd
                    removePatternAtEnd(name, dirPath, patternToBeRemoved, renamedList)

                else:
                    removeDefaultPattern(name, dirPath, renamedList)

            #Print all directories in current directory
            for name in dirs:
                fold = os.path.join(dirPath, name)
                print('Folder: '+fold)

    else:
         print('Path is not valid')

    if renamedList:
         print('Files renamed: ')
         for name in renamedList:
             print(name)
         print('Successfully rename '+str(len(renamedList))+' file/s')





if __name__ == '__main__':
    main()

