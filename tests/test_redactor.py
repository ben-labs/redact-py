import pytest
from redactor.redactor import Redactor

@pytest.fixture
def obj():
    return Redactor()


def test_check_python_file(obj):
    assert obj.check_file_type(__file__) == 'text/x-python', 'Failed python file check'


def test_check_text_type(obj):
    assert obj.check_file_type('dev-requirements.txt') == 'text/plain', 'Failed text file check'


def test_number_of_allowed_types(obj):
    assert len(obj.get_allowed_files()) == 10, 'Number of allowed tests does not match expected'


def test_current_file_is_allowed(obj):
    assert obj.allowed_file(__file__), f'{__file__} should be allowed'
