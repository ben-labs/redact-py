#!/usr/bin/env python
'''
Utility to redact files
'''
import argparse
import sys
import os

from redactor.redactor import Redactor


def main():
    '''Main calling function for cli
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Logfile to process')
    parser.add_argument('-r', '--rulefile', help='Ruleset file')
    parser.add_argument('-o', '--outpath', help="Output file path")
    args = parser.parse_args()

    # check if file is there
    if not os.path.isfile(args.filename):
        sys.exit(f"[ - ] {args.filename} not present")

    # redact file
    if args.rulefile:
        red_obj = Redactor(args.rulefile)
    else:
        red_obj = Redactor()

    if args.outpath:
        red_obj.execute(args.filename, args.outpath)
    else:
        red_obj.execute(args.filename)


if __name__ == '__main__':
    main()
