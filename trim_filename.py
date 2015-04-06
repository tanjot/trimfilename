#!/usr/bin/python3
import sys
import os
import re
import argparse
#renamed =[]

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

    for name in argu.path:
        print(name)
        parseDir(name,argu)

def renameFile(oldname, nameList, dirPath, renamedList):
    ''' Renames file if name has changed
    '''
    pathNname = os.path.join(dirPath, oldname)

    newname = ''
    #Does not rename file if it begins with '.' or the whole file name gets
    #deleted after rename and also if there is no change in filename
    if nameList and nameList[0] != '.' and oldname != ''.join(nameList):
        newname = ''.join(nameList)
        os.rename(pathNname, os.path.join(dirPath, newname))
        print('Successfully renamed '+pathNname+' to'
               ' '+ newname)

        #adding filename to common list of renamed files
        renamedList.append(pathNname + ' to ' + newname)

    else:
        print('Not renaming, filename : '+pathNname)

def removeDefaultPattern(name, dirPath, renamedList):
    ''' storing name in a list for manipulations on characters individually
    '''
    #print('Processing file: '+pathNname)
    nameList = list(name)

    #To not rename files starting with only '.'
    if nameList[0] != '.':
        for char in name:
            #remove all non alphabet characters from filename
            if not(char.isalpha() or char == '.'):
                del(nameList[nameList.index(char)])
            else:
                break

        renameFile(name, nameList, dirPath, renamedList)

def removePatternAtBeg(name, dirPath, patternToBeRemoved, renamedList):
    ''' Removes the pattern matched at beginning of the filename
    '''
    patternLi = list(patternToBeRemoved)

    #will not rename extension or hidden files
    if name[0] != '.':

        newname = name[len(patternToBeRemoved):]

        #will not rename if the whole filename is deleted or starts with a
        #after rename
        if newname and newname[0] != '.' and name != newname:
            oldPathName = os.path.join(dirPath, name)

            print('Successfully renamed '+oldPathName+' to'
                   ' '+ newname)

            os.rename(oldPathName, os.path.join(dirPath,
                newname))

            #adding filename to common list of renamed files
            renamedList.append(oldPathName + ' to ' + newname)

def parseDir(fname, argu):
   print('Entered parseDirfname'+fname)

   renamedList = []
   if os.path.exists(fname):
       for dirPath, dirs, files in os.walk(fname):

           for name in files:
               if argu.patternInString:
                   patternToBeRemoved = argu.patternInString
                   print('Find pattern: ' + patternToBeRemoved)
                   match = re.search(patternToBeRemoved+'\w+', name)
                   #removePatternInString()
               elif argu.patternAtBeg:
                   #print('Find pattern: '+ argu.patternAtBeg +' at beginning')

                   patternToBeRemoved = argu.patternAtBeg
                   match = re.search('^' + patternToBeRemoved, name)
                   if match:
                       print('PATT AT BEG: '+ match.group() +' filename: '+name);
                       removePatternAtBeg(name, dirPath, patternToBeRemoved,
                               renamedList)

               elif argu.patternAtEnd:
                   patternToBeRemoved = argu.patternAtEnd
                   print('Find pattern: '+ patternToBeRemoved +' at end')
               else:
                   #pattern = r'^[\[+ \]+ \d+ _+\s+ -+]+'#^\d+]+'
                   removeDefaultPattern(name, dirPath, renamedList)

   else:
        print('Path is not valid')

   if renamedList:
       print('Files renamed: ')
       for name in renamedList:
           print(name)
       print('Successfully rename '+str(len(renamedList))+' file/s')

   for name in dirs:
       fold = os.path.join(dirPath, name)
       print('Folder: '+fold)

if __name__ == '__main__':
    main()

