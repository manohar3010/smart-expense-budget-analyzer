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
    
    def calculate_category_percentages(self):
        """Calculate the percentage contribution of each category."""

        total = self.calculate_total_expenses()

        if total == 0:
            return {}

        category_totals = self.calculate_category_expenses()

        percentages = {}

        for category, amount in category_totals.items():
            percentages[category] = (amount / total) * 100

        return percentages
    
    def find_large_expenses(self, threshold=1000):
        """Find expenses above a specified amount."""

        large_expenses = []

        for expense in self.expenses:

            if float(expense["amount"]) >= threshold:
                large_expenses.append(expense)

        return large_expenses

    def compare_months(self, current_month, previous_month):
        """Compare spending between two months."""

        monthly_totals = self.calculate_monthly_expenses()

        current_amount = monthly_totals.get(
            current_month,
            0
        )

        previous_amount = monthly_totals.get(
            previous_month,
            0
        )

        if previous_amount == 0:
            return {
                "current": current_amount,
                "previous": previous_amount,
                "difference": current_amount,
                "percentage_change": 0
            }

        difference = current_amount - previous_amount

        percentage_change = (
            difference / previous_amount
        ) * 100

        return {
            "current": current_amount,
            "previous": previous_amount,
            "difference": difference,
            "percentage_change": percentage_change
        }
    def get_category_budget_status(
        self,
        category_budgets):
        """Compare category spending with category budgets."""

        category_totals = self.calculate_category_expenses()

        status = {}

        for category, budget in category_budgets.items():

            spent = category_totals.get(
                category,
                0
            )

            remaining = budget - spent

            if budget > 0:
                usage = (spent / budget) * 100
            else:
                usage = 0

            status[category] = {
                "budget": budget,
                "spent": spent,
                "remaining": remaining,
                "usage": usage
            }

        return status
    


