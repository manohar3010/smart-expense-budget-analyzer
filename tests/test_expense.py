import unittest
import os

from src.expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        self.test_file = "data/test_expenses.csv"

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        self.manager = ExpenseManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_expense(self):
        result = self.manager.add_expense(
            "24-09-2026",
            "Food",
            "250",
            "Lunch",
            "UPI"
        )

        self.assertTrue(result[0])
        self.assertEqual(len(self.manager.expenses), 1)

    def test_invalid_amount(self):
        result = self.manager.add_expense(
            "24-09-2026",
            "Food",
            "-100",
            "Lunch",
            "UPI"
        )

        self.assertFalse(result[0])


if __name__ == "__main__":
    unittest.main()