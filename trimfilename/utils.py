import os

class PatternLocations:
    patternAtBeg = 1
    patternAtEnd = 2
    patternInString = 3


def renameFile(oldname, newname, dirPath):
    ''' Renames file if name has changed
    '''

    changed_file_name = False
    old_file_path = os.path.join(dirPath, oldname)

    #Does not rename file if it begins with '.' or the whole file name gets
    #deleted after rename and also if there is no change in filename
    if newname and newname[0] != '.' and oldname != newname:
        os.rename(old_file_path, os.path.join(dirPath, newname))
        #print('Successfully renamed '+pathNname+' to'
        #       ' '+ newname)

        changed_file_name = True

    return changed_file_name