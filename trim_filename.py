#!/usr/bin/python3
import sys
import os
import re
import argparse
pattern = ''#= r'^[\[+ \]+ \d+ _+ .+ \s+ -+]+'
renamed =[]

#define function main
def main(arg = sys.argv):
    #initializing argument parser
    parser = argparse.ArgumentParser()
    #adding arguments
    parser.add_argument("path", help="Give the path name to rename files",
            type=str, nargs='+')
    parser.add_argument("-p", "--pattern", help="Give the pattern that is to "
                "be removed", type=str)
    parser.add_argument("-pb", "--patternAtBeg", help="Pattern to be removed "
                "is matched at beginning of the filenames", type=str)
    parser.add_argument("-pe", "--patternAtEnd", help="Pattern to be removed "
                "is matched at end of the filenames(extension should be "
                "included in pattern)", type=str)


    #parsing arguments
    argu = parser.parse_args()

    global pattern
    for name in argu.path:
        print(name)
        parseDir(name,argu)

def renameFile(oldname, renamedList, dirPath):
    ''' Renames file if name has changed
    '''
    pathNname = os.path.join(dirPath, oldname)

    newname = ''
    #Does not rename file if it begins with '.' or the whole file name gets
    #deleted after rename and also if there is no change in filename
    if renamedList and renamedList[0] != '.' and oldname != ''.join(renamedList):
        newname = ''.join(renamedList)
        os.rename(pathNname, os.path.join(dirPath, newname))
        print('Successfully renamed '+pathNname+' to'
               ' '+ newname)

        #adding filename to common list of renamed files
        renamed.append(pathNname + ' to ' + newname)

    else:
        print('Not renaming, filename : '+pathNname)

def removeDefaultPattern(name, dirPath):
    ''' storing name in a list for manipulations on characters individually
    '''
    #print('Processing file: '+pathNname)
    li = list(name)

    #To not rename files starting with only '.'
    if li[0] != '.':
        for char in name:
            #remove all non alphabet characters from filename
            if not(char.isalpha() or char == '.'):
                del(li[li.index(char)])
            else:
                break

        renameFile(name, li, dirPath)

def removePatternAtBeg(name, dirPath):
    ''' Removes the pattern matched at beginning of the filename
    '''
    li = list(name)
    patternLi = list(pattern)
    global renamed

    #will not rename extension or hidden files
    if li[0] != '.':

        newname = name[len(pattern):]

        #will not rename if the whole filename is deleted or starts with a
        #after rename
        if newname and newname[0] != '.' and name != newname:
            oldPathName = os.path.join(dirPath, name)

            print('Successfully renamed '+oldPathName+' to'
                   ' '+ newname)

            os.rename(oldPathName, os.path.join(dirPath,
                newname))

            #adding filename to common list of renamed files
            renamed.append(oldPathName + ' to ' + newname)

def parseDir(fname, argu):
   print('Entered parseDirfname'+fname)

   if os.path.exists(fname):
       for dirPath, dirs, files in os.walk(fname):

           for name in files:
               global pattern
               if argu.pattern:
                   print('Find pattern: ' + pattern)
                   pattern = argu.pattern
                   match = re.search(pattern+'\w+', name)
               elif argu.patternAtBeg:
                   #print('Find pattern: '+ argu.patternAtBeg +' at beginning')

                   match = re.search('^' + argu.patternAtBeg  , name)
                   if match :
                       print('PATT AT BEG: '+ match.group() +' filename: '+name);
                       pattern = argu.patternAtBeg
                       removePatternAtBeg(name, dirPath)

               elif argu.patternAtEnd:
                   print('Find pattern: '+ pattern +' at end')
               else:
                   #pattern = r'^[\[+ \]+ \d+ _+\s+ -+]+'#^\d+]+'
                   removeDefaultPattern(name, dirPath)

   else:
        print('Path is not valid')

   global renamed
   if renamed:
       print('Files renamed: ')
       for f in renamed:
           print(f)
       print('Successfully rename '+str(len(renamed))+' file/s')

   for name in dirs:
       fold = os.path.join(dirPath, name)
       print('Folder: '+fold)

if __name__ == '__main__':
    main()

