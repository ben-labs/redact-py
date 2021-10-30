#!/usr/bin/env python
'''
Utility to redact files
'''
import argparse
import mimetypes
import sys
import os
import time
import re


def is_text_file(filepath):
    '''
    Check file type
    '''
    if mimetypes.guess_type(filepath)[0] == 'text/plain':
        return True
    print(mimetypes.guess_type(filepath)[0])
    return False


def redact_file(filename, patterns):
    '''
    Redact file
    '''
    count = 0
    start = time.time()
    with open(filename, encoding="utf-8") as fP:
        with open('redacted_' + os.path.basename(filename),
                  'w',
                  encoding="utf-8") as w:
            for line in fP:
                for p in patterns:
                    if re.search(p['pattern'], line, re.IGNORECASE):
                        line = re.sub(p['pattern'], p['mask'], line)
                w.write(line)
                count = count + 1
    end = time.time()
    print(f"Processed {count} records...")
    tt = end - start
    print(f'Took {tt} seconds to execute')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Logfile to process')
    parser.add_argument('--rulefile', help='Ruleset file')
    args = parser.parse_args()

    # check if file is there
    if not os.path.isfile(args.filename):
        sys.exit(f"{args.filename} not present")

    # check if file is a text file
    # if not is_text_file(filename):
    #     sys.exit(f"{filename} is not a text file")

    # read pattern file
    redact_file(args.filename, [
        {
            "pattern": r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',
            "mask": "XXX.XXX.XXX.XXX",
        }
    ])
