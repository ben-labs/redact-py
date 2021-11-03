import os
import mimetypes
import json
import sys
import time
import re


class Redactor:
    def __init__(self, rulefile=None) -> None:
        self.__load_allowed_files__()
        if rulefile is None:
            self.__read_rules__()
        else:
            self.__read_rules__(rulefile)

    def check_file_type(self, file):
        if not os.path.isfile(file):
            return (None, None)
        return mimetypes.guess_type(file)[0]

    def __load_allowed_files__(self):
        with open('redactor/allowed_types.dat', encoding="utf-8") as fp:
            self.allowed_files = fp.read().split('\n')

    def get_allowed_files(self):
        return self.allowed_files

    def allowed_file(self, file):
        if not os.path.isfile(file):
            return False
        return mimetypes.guess_type(file)[0] in self.get_allowed_files()

    def __read_rules__(self, ruleFile='default_rules.conf'):
        '''
        Read a json rule file and return a json object
        '''
        try:
            with open(ruleFile) as fP:
                self.patterns = json.load(fP)
        except FileNotFoundError:
            sys.exit("[ - ] Rule file was not found")
        except json.JSONDecodeError:
            sys.exit("[ - ] Issue decoding rule file")

    def redact_file(self, filename, filepath='./'):
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
                        for p in self.patterns:
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
