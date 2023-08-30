import unittest
import sqlite3
from unittest.mock import patch
from model import CalculatorModel

class TestCalculatorModel(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorModel()

    def test_calculate_expresion(self):
        self.assertEqual(self.calculator.calculate_expression('3+1'), '4')
        self.assertEqual(self.calculator.calculate_expression('9/3'), '3.0')

    def test_add_record_to_db(self):
        expression = "2 + 2"
        result = "4"

        self.calculator.add_record_to_db(expression, result)

        records = self.calculator.load_history_db()
        last_record = records[-1] if records else None

        self.assertIsNotNone(last_record)
        self.assertEqual(last_record[0], expression)
        self.assertEqual(last_record[1], result)

    def test_load_history_db(self):
        self.calculator.add_record_to_db("2 + 2", "4")
        self.calculator.add_record_to_db("3 * 5", "15")

        loaded_records = self.calculator.load_history_db()

        self.assertIn(("2 + 2", "4"), loaded_records)
        self.assertIn(("3 * 5", "15"), loaded_records)


if __name__ == '__main__':
    unittest.main()
