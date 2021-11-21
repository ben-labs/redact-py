<p align="center">
    <h1>CLI tool to enable redaction of sensitive information.</h1>
</p>
<p align="center">
    <em>Data redaction tool for text files</em>
</p>
<p align="center">
<!-- <a href="https://github.com/ben-labs/redact-py/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/ben-labs/redact-py/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a> -->
<img alt="Tested with Bandit" src="https://img.shields.io/badge/Bandit-Tested-blue">
<a href="https://pypi.org/project/redactor2" target="_blank">
<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/ben-labs/redact-py?style=plastic">
</a>
</p>
### Sample command
`./redact.py --outfile redacted --rulefile sample_rule.conf  <target file>`

### Sample Files
- [itcont.txt - 4GB uncompressed](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/itcont.tar.gz)
- [test_sample2.txt - 10002 lines of IP addresses](https://sanitizationbq.s3.ap-southeast-1.amazonaws.com/test_sample2.txt)
