from colorama import Fore

import os

class PatternLocations:
    patternAtBeg = 1
    patternAtEnd = 2
    patternInString = 3


def rename_file(oldname, newname, dirPath):
    """ Renames file if name has changed
    """

    changed_file_name = False

    if oldname != newname:
        old_file_path = os.path.join(dirPath, oldname)
        if os.path.exists((os.path.join(dirPath, newname))) is False:
            if (newname and (newname.find('.') != -1) and newname[0] != '.' and
                 (len(oldname)-oldname.rfind('.')) == (len(newname)-newname.rfind('.'))):

                # Does not rename file if it begins with '.' or the whole file name gets
                # deleted after rename, also if there is no change in filename or the extension has been changed
                os.rename(old_file_path, os.path.join(dirPath, newname))
                changed_file_name = True
            else:
                print('Could not rename ' + old_file_path + ' to ' + Fore.YELLOW + newname)
                print('There was probably some issue with extension\n')
        else:
            print('File '+old_file_path+' cannot be renamed, '+ Fore.YELLOW + newname+' already exists')

    return changed_file_name
