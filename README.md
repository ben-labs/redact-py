<p align="center">
    <h1>CLI tool to enable redaction of sensitive information.</h1>
</p>
<p align="center">
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/ben-labs/redact-py/Pylint?label=pylint&style=plastic">
<img alt="Tested with Bandit" src="https://img.shields.io/badge/Bandit-Tested-blue?style=plastic">
<a href="https://pypi.org/project/redactor2" target="_blank">
<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/ben-labs/redact-py?style=plastic">
</a>
</p>

## Description
<p align="center">
    <em>Data redaction tool for text files</em>
    <br>
    <P>
    This tool will help you ensure that sensitive information is not unintentionally sent out of your organization.
    </p> 
    <p>
    There are times that troubleshooting issues may require your vendor to analyse your log files. Ideally sensitive information such as IP addresses, hostnames, email addresses and even personal information might need to be redacted / masked.
    </p>
    <p>
    Most of the time, redacting such information is reliant on the engineer eyeballing / searching and replacing sensitive information. Needless to say this is prone to human error and can sometimes take up a lot of an engineer's time.
    </p>
    <p>
    Redactor helps by maintaining a repository of patterns that can be used over and over again to redact files in seconds. Tested timings on redacting a 4GB log file takes less than a minute
    </p>
    <p>
    The tool is configured so that developers may expand on this by using redactor as a module. Or users may just opt to install the tool and run the tool in command line.
    </p>
</p>

## Installation
### On command prompt (windows should be similar)
1. `$ git clone https://github.com/ben-labs/redact-py.git`
2. `$ cd redact-py`
3. `$ pip install .`

### Checking if installation was properly done
`$ redactor -h`

#### You should see the help file as below:
![Alt](/images/redactor-help.png "Title")


## Usage:
### Basic Redacting
1. `$ redactor test_sample2.txt`
2. ![Basic Redaction](/images/basic_redact.png "Basic Redaction")

Sample Result:
![Sample](/images/sample.png "Sample")

## Rule files
You can create your own rule files and feed it to redactor with the -r flag.
Sample of what a redaction rule file will look like:

[Sample Rule File](sample_rule.conf)

| Attribute   | Description                          |
| ----------- | ------------------------------------ |
| pattern     | Regex pattern of string to find      |
| mask        | Replace found patterns with the mask |
| Description | Non-Mandatory description            |
|||

## Optional Flags usable:
| Flag                              | Description                                                                       |
| --------------------------------- | --------------------------------------------------------------------------------- |
| -h, --help                        | Displays help message                                                             |
| -r RULEFILE, --rulefile RULEFILE  | Sets a custom rulefile                                                            | 
| -o OUTPATH, --outpath OUTPATH     | Specify a directory to dump redacted files. Creates one if directory is not there.|
|||

## Sample Files
- [itcont.txt - 4GB uncompressed](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/itcont.tar.gz)
- [test_sample2.txt - 10002 lines of IP addresses](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/test_sample2.txt)
