import unittest

from src.analytics import ExpenseAnalytics


class TestExpenseAnalytics(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {
                "expense_id": "E001",
                "date": "24-09-2026",
                "category": "Food",
                "amount": "250",
                "description": "Lunch",
                "payment_method": "UPI"
            },
            {
                "expense_id": "E002",
                "date": "24-09-2026",
                "category": "Transport",
                "amount": "100",
                "description": "Bus",
                "payment_method": "Cash"
            }
        ]

        self.analytics = ExpenseAnalytics(self.expenses)

    def test_total_expenses(self):
        total = self.analytics.calculate_total_expenses()

        self.assertEqual(total, 350)

    def test_highest_category(self):
        category = self.analytics.find_top_category()

        self.assertEqual(category, "Food")

    def test_category_percentages(self):
        percentages = self.analytics.calculate_category_percentages()

        self.assertAlmostEqual(percentages["Food"], 71.43, places=1)


if __name__ == "__main__":
    unittest.main()