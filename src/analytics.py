from collections import defaultdict
from datetime import datetime


class ExpenseAnalytics:

    def __init__(self, expenses):
        self.expenses = expenses

    def calculate_total_expenses(self):
        """Calculate total amount spent."""

        total = 0

        for expense in self.expenses:
            total += float(expense["amount"])

        return total

    def calculate_category_expenses(self):
        """Calculate expenses category-wise."""

        category_totals = defaultdict(float)

        for expense in self.expenses:

            category = expense["category"]
            amount = float(expense["amount"])

            category_totals[category] += amount

        return dict(category_totals)

    def calculate_monthly_expenses(self):
        """Calculate expenses month-wise."""

        monthly_totals = defaultdict(float)

        for expense in self.expenses:

            date = datetime.strptime(
                expense["date"],
                "%d-%m-%Y"
            )

            month = date.strftime("%m-%Y")

            amount = float(expense["amount"])

            monthly_totals[month] += amount

        return dict(monthly_totals)

    def calculate_average_daily_expense(self):
        """Calculate average spending per day."""

        if not self.expenses:
            return 0

        total = self.calculate_total_expenses()

        dates = set()

        for expense in self.expenses:
            dates.add(expense["date"])

        number_of_days = len(dates)

        if number_of_days == 0:
            return 0

        return total / number_of_days

    def find_highest_expense(self):
        """Find the highest individual expense."""

        if not self.expenses:
            return None

        return max(
            self.expenses,
            key=lambda expense: float(expense["amount"])
        )

    def find_top_category(self):
        """Find the category with the highest spending."""

        category_totals = self.calculate_category_expenses()

        if not category_totals:
            return None

        return max(
            category_totals,
            key=category_totals.get
        )

    def calculate_budget_usage(self, monthly_budget):
        """Calculate percentage of budget used."""

        if monthly_budget <= 0:
            return 0

        total = self.calculate_total_expenses()

        return (total / monthly_budget) * 100