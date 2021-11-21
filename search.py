#!/usr/bin/env python
'''
Utility to search for files with contents to be redacted
'''
import argparse
import os

from redactor.redactor import Search

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help="path to scan")
    parser.add_argument('-r', '--rulefile', help='Ruleset file')
    parser.add_argument('-o', '--outpath', help="Output file path")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        if args.rulefile:
            srch = Search(args.rulefile)
        else:
            srch = Search()

        if args.outpath:
            srch.execute(args.path, args.outpath)
        else:
            srch.execute(args.path)
