#!/usr/bin/env python
'''
Utility to redact files
'''
import argparse
import sys
import os
import time
import re
import json


def read_rules(ruleFile):
    '''
    Read a json rule file and return a json object
    '''
    try:
        with open(ruleFile) as fP:
            jData = json.load(fP)
            return jData
    except FileNotFoundError:
        sys.exit("[ - ] Rule file was not found")
    except json.JSONDecodeError:
        sys.exit("[ - ] Issue decoding rule file")


def redact_file(filename, patterns, filepath='./'):
    '''
    Redact file
    '''
    count = 0
    redact_count = 0
    start = time.time()
    try:
        with open(filename, encoding="utf-8") as fP:
            # Check the format of the output directory
            if filepath != './' and filepath[-1] != '/':
                filepath = filepath + '/'

            # created the directory if not there
            if not os.path.exists(os.path.dirname(filepath)):
                print("[ + ] " + os.path.dirname(filepath) +
                      " directory does not exist... Creating it")
                os.makedirs(os.path.dirname(filepath))

            print("[ + ] Processing starts now. This may take some time "
                  "depending on the file size. Monitor the redacted file "
                  "size to monitor progress")
            with open(f"{filepath}redacted_{os.path.basename(filename)}",
                      'w',
                      encoding="utf-8") as w:
                for line in fP:
                    # # print a . for every 1000 processed
                    # if count % 1000 == 0:
                    #     print('.', end='')
                    for p in patterns:
                        if re.search(p['pattern'], line, re.IGNORECASE):
                            line = re.sub(p['pattern'], p['mask'], line,
                                          flags=re.IGNORECASE)
                            redact_count = redact_count + 1
                    w.write(line)
                    count = count + 1
        end = time.time()
        print()
        print(f"[ + ] Processed {count} records...")
        print(f"[ + ] Redacted {redact_count} targets...")
        tt = end - start
        print(f'[ + ] Took {tt} seconds to execute')
    except UnicodeDecodeError:
        # remove the created file
        os.remove(f"{filepath}redacted_{os.path.basename(filename)}")
        print("[ - ] Removed incomplete redact file")
        sys.exit("[ - ] Unable to read file")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Logfile to process')
    parser.add_argument('-r', '--rulefile', help='Ruleset file')
    parser.add_argument('-o', '--outfile', help="Output file path")
    args = parser.parse_args()

    # check if file is there
    if not os.path.isfile(args.filename):
        sys.exit(f"[ - ] {args.filename} not present")

    # read pattern file
    if args.rulefile:
        rules = read_rules(args.rulefile)
    else:
        rules = read_rules('default_rules.conf')

    # redact file
    if args.outfile:
        redact_file(args.filename, rules, args.outfile)
    else:
        redact_file(args.filename, rules)
