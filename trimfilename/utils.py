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
                # deleted after rename and also if there is no change in filename
                os.rename(old_file_path, os.path.join(dirPath, newname))
                # print('Successfully renamed '+pathNname+' to'
                #       ' '+ newname)

                changed_file_name = True
        # else log for extension changed

    return changed_file_name
