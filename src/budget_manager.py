import json
import os


class BudgetManager:

    def __init__(self, file_path="data/budget.json"):
        self.file_path = file_path
        self.budget = {
            "monthly_budget": 0,
            "category_budgets": {}
        }

        self.load_budget()

    def load_budget(self):
        """Load budget information from JSON file."""

        if not os.path.exists(self.file_path):
            self.save_budget()
            return

        try:
            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.budget = json.load(file)

        except (json.JSONDecodeError, OSError):

            self.budget = {
                "monthly_budget": 0,
                "category_budgets": {}
            }

    def save_budget(self):
        """Save budget information to JSON file."""

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.budget,
                file,
                indent=4
            )

    def set_monthly_budget(self, amount):
        """Set the overall monthly budget."""

        try:
            amount = float(amount)

            if amount <= 0:
                return False, "Budget must be greater than zero."

        except ValueError:
            return False, "Budget must be a valid number."

        self.budget["monthly_budget"] = amount

        self.save_budget()

        return True, "Monthly budget updated successfully."

    def set_category_budget(self, category, amount):
        """Set a budget for a specific category."""

        try:
            amount = float(amount)

            if amount <= 0:
                return False, "Budget must be greater than zero."

        except ValueError:
            return False, "Budget must be a valid number."

        category = category.title()

        self.budget["category_budgets"][category] = amount

        self.save_budget()

        return True, f"Budget for {category} updated successfully."

    def get_monthly_budget(self):
        """Return monthly budget."""

        return self.budget["monthly_budget"]

    def get_category_budgets(self):
        """Return category budgets."""

        return self.budget["category_budgets"]

    def get_category_budget(self, category):
        """Return budget for a specific category."""

        return self.budget["category_budgets"].get(
            category.title(),
            0
        )