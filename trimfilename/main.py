#!/usr/bin/python3

import sys
import argparse

from .trimfilename import TrimFilename
from .utils import PatternLocations

def main():
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

    pattern_location = None
    pattern = None

    if argu.patternInString:
        pattern_location = PatternLocations.patternInString
        pattern = argu.patternInString
    elif argu.patternAtBeg:
        pattern_location = PatternLocations.patternAtBeg
        pattern = argu.patternAtBeg
    elif argu.patternAtEnd:
        pattern_location = PatternLocations.patternAtEnd
        pattern = argu.patternAtEnd


    trimfilename_handle = TrimFilename(pattern_location, pattern)
    #TODO: not pass argu as parameter
    for name in argu.path:
        print(name)
        trimfilename_handle.parseDir(name)

if __name__ == '__main__':
    sys.exit(main())