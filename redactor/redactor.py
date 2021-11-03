import os
import mimetypes
import json
import sys
import time
import re


class Redactor:
    '''Redactor class

    Class containing all methods to support redaction
    of sensitive data
    '''

    def __init__(self, rulefile=None) -> None:
        '''Class Initialization

        Args:
            rulefile (str): Rulefile name

        Returns:
            None
        '''
        self.__load_allowed_files__()
        if rulefile is None:
            self.__read_rules__()
        else:
            self.__read_rules__(rulefile)

    def check_file_type(self, file):
        '''Checks for the supplied file type

        Args:
            file (str): Filename of file to check

        Returns:
            mime (str): Mime type
        '''
        if not os.path.isfile(file):
            return (None, None)
        return mimetypes.guess_type(file)[0]

    def __load_allowed_files__(self):
        '''Helper function to load pre-defined allowed files

        Sets allowed_files with list of allowed file types read
        from allowed_types.dat

        Args:
            None

        Returns:
            None
        '''
        with open('redactor/allowed_types.dat', encoding="utf-8") as fp:
            self.allowed_files = fp.read().split('\n')

    def get_allowed_files(self):
        '''Gets a list of allowed files

        Args:
            None

        Returns:
            allowed_file (list): List of allowed files
        '''
        return self.allowed_files

    def allowed_file(self, file):
        '''Checks if supplied file is allowed

        Checks the supplied file to see if it is in the allowed_files list

        Args:
            file (str): File to check

        Returns:
            False: File not found / File type is not allowed
            True: File is allowed
        '''
        if not os.path.isfile(file):
            return False
        return mimetypes.guess_type(file)[0] in self.get_allowed_files()

    def __read_rules__(self, ruleFile='default_rules.conf'):
        '''Load Rules

        Loads either a default ruleset or a self defined ruleset.
        Rules are loaded to patterns variable

        Args:
            ruleFile (str): Custom rule file to be loaded

        Returns:
            None
        '''
        try:
            with open(ruleFile) as fP:
                self.patterns = json.load(fP)
        except FileNotFoundError:
            sys.exit("[ - ] Rule file was not found")
        except json.JSONDecodeError:
            sys.exit("[ - ] Issue decoding rule file")

    def redact_file(self, filename, filepath='./'):
        '''Main redact function

        Main function to redact a file

        Args:
            filename (str): File to redact
            filepath (str): [Optional] filepath to place results

        Returns:
            None
        '''
        count = 0
        redact_count = 0
        start = time.time()
        try:
            # Open a file read pointer fP
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

                # Open a file write pointer w
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
