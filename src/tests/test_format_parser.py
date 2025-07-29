
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from core.format_parser import FormatParser
from core.type_detector import DataTypeDetector
import unittest
import pandas as pd
class TestFormatParser(unittest.TestCase):
    def setUp(self):
        self.parser = FormatParser()

    def test_parse_amount(self):
        self.assertEqual(self.parser.parse_amount("$1,000.50"), 1000.50)
        self.assertEqual(self.parser.parse_amount("(2,000.00)"), -2000.00)
        self.assertEqual(self.parser.parse_amount("1.5M"), 1500000.0)
        self.assertEqual(self.parser.parse_amount("₹1,23,456"), 123456.0)

    def test_parse_date(self):
        self.assertEqual(str(self.parser.parse_date("44927")), "2023-01-01")
        self.assertEqual(str(self.parser.parse_date("2023-12-31")), "2023-12-31")

if __name__ == '__main__':
    unittest.main()
