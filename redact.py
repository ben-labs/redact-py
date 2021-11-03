#!/usr/bin/env python
'''
Utility to redact files
'''
import argparse
import sys
import os

from redactor.redactor import Redactor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Logfile to process')
    parser.add_argument('-r', '--rulefile', help='Ruleset file')
    parser.add_argument('-o', '--outpath', help="Output file path")
    # parser.add_argument('-f', '--filter',
    #                     help="Output only redacted items", action='store_true')
    # parser.add_argument('-e', '--export',
    #                     help="Export without redacting", action="store_true")
    args = parser.parse_args()

    # check if file is there
    if not os.path.isfile(args.filename):
        sys.exit(f"[ - ] {args.filename} not present")

    # redact file
    if args.rulefile:
        redObj = Redactor(args.rulefile)
    else:
        redObj = Redactor()

    if args.outpath:
        redObj.execute(args.filename, args.outpath)
    else:
        redObj.execute(args.filename)
