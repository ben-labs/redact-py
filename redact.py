#!/usr/bin/env python
'''
Utility to redact files
'''
import argparse
import os
import glob

from redactor.redactor import Redactor


def main():
    '''Main calling function for cli
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', help='Path to file or files.')
    parser.add_argument('-r', '--rulefile', help='Ruleset file')
    parser.add_argument('-o', '--outpath', help="Output file path")
    parser.add_argument('-s', '--subfolders', action='store_true',
                        default=True, help='Search through subfolders')
    parser.add_argument('-e', '--extension', default='',
                        help='File extension to filter by.')
    args = parser.parse_args()

    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()

    for path in full_paths:
        if os.path.isfile(path):
            file_name, file_ext = os.path.splitext(path)
            if args.extension == '' or args.extension == file_ext:
                files.add(path)
        else:
            if (args.subfolders):
                full_paths += glob.glob(path + '/*')

    # redact file

    if args.rulefile:
        red_obj = Redactor(args.rulefile)
    else:
        red_obj = Redactor()

    for file in files:
        if args.outpath:
            red_obj.execute(file, args.outpath)
        else:
            red_obj.execute(file)


if __name__ == '__main__':
    main()
