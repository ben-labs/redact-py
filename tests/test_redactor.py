import unittest
from redactor.redactor import Redactor
class TestRedactor(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Redactor()
        return super().setUp()
    
    def test_check_file_type(self):
        testfile = __file__
        self.assertEqual(self.obj.check_file_type(testfile), 'text/x-python', "Not an allowed file")

    def test_allowed_types(self):
        ary = self.obj.get_allowed_files()
        self.assertEqual(len(ary), 10, "Testing expected amount of allowed files")
        self.assertTrue(self.obj.allowed_file(__file__), "test_allowed_types failed")
