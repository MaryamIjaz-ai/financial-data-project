import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from core.type_detector import DataTypeDetector
import unittest
import pandas as pd

class TestTypeDetector(unittest.TestCase):
    def setUp(self):
        self.detector = DataTypeDetector()

    def test_numeric_detection(self):
        series = pd.Series(["100", "200", "300"])
        result = self.detector.detect_column_type(series)
        self.assertEqual(result["type"], "number")

    def test_date_detection(self):
        series = pd.Series(["2023-01-01", "01/02/2023", "March 5, 2023"])
        result = self.detector.detect_column_type(series)
        self.assertEqual(result["type"], "date")

if __name__ == '__main__':
    unittest.main()
