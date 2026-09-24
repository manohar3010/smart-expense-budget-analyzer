import csv
import os

from src.utils import generate_expense_id
from src.validator import (
    validate_amount,
    validate_date,
    validate_category,
    validate_payment_method
)


class ExpenseManager:

    def __init__(self, file_path="data/expenses.csv"):
        self.file_path = file_path
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from CSV file."""
        self.expenses = []

        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.expenses.append(row)

    def save_expenses(self):
        """Save expenses to CSV file."""
        fieldnames = [
            "expense_id",
            "date",
            "category",
            "amount",
            "description",
            "payment_method"
        ]

        with open(
            self.file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(
        self,
        date,
        category,
        amount,
        description,
        payment_method
    ):
        """Add a new expense."""

        valid, message = validate_date(date)

        if not valid:
            return False, message

        valid, message = validate_amount(amount)

        if not valid:
            return False, message

        valid, message = validate_category(category)

        if not valid:
            return False, message

        valid, message = validate_payment_method(payment_method)

        if not valid:
            return False, message

        expense = {
            "expense_id": generate_expense_id(self.expenses),
            "date": date,
            "category": category.title(),
            "amount": f"{float(amount):.2f}",
            "description": description.strip(),
            "payment_method": payment_method.title()
        }

        self.expenses.append(expense)
        self.save_expenses()

        return True, expense["expense_id"]

    def view_expenses(self):
        """Return all expenses."""
        self.load_expenses()
        return self.expenses

    def find_expense(self, expense_id):
        """Find an expense using its ID."""

        self.load_expenses()

        for expense in self.expenses:
            if expense["expense_id"].upper() == expense_id.upper():
                return expense

        return None

    def update_expense(
        self,
        expense_id,
        date,
        category,
        amount,
        description,
        payment_method
    ):
        """Update an existing expense."""

        self.load_expenses()

        expense = self.find_expense(expense_id)

        if expense is None:
            return False, "Expense not found."

        valid, message = validate_date(date)

        if not valid:
            return False, message

        valid, message = validate_amount(amount)

        if not valid:
            return False, message

        valid, message = validate_category(category)

        if not valid:
            return False, message

        valid, message = validate_payment_method(payment_method)

        if not valid:
            return False, message

        expense["date"] = date
        expense["category"] = category.title()
        expense["amount"] = f"{float(amount):.2f}"
        expense["description"] = description.strip()
        expense["payment_method"] = payment_method.title()

        self.save_expenses()

        return True, "Expense updated successfully."

    def delete_expense(self, expense_id):
        """Delete an expense."""

        self.load_expenses()

        for index, expense in enumerate(self.expenses):

            if expense["expense_id"].upper() == expense_id.upper():

                deleted = self.expenses.pop(index)

                self.save_expenses()

                return True, deleted

        return False, "Expense not found."

    def search_expenses(self, keyword):
        """Search expenses by description or category."""

        self.load_expenses()

        keyword = keyword.lower()

        results = []

        for expense in self.expenses:

            if (
                keyword in expense["description"].lower()
                or keyword in expense["category"].lower()
            ):
                results.append(expense)

        return results

    def filter_by_category(self, category):
        """Filter expenses by category."""

        self.load_expenses()

        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        ]