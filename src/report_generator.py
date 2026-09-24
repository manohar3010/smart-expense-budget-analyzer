import csv
import os
from datetime import datetime


class ReportGenerator:

    def __init__(
        self,
        analytics,
        budget_manager,
        output_directory="reports"
    ):

        self.analytics = analytics
        self.budget_manager = budget_manager
        self.output_directory = output_directory

        os.makedirs(
            self.output_directory,
            exist_ok=True
        )

    def generate_monthly_report(self):
        """Generate monthly expense report."""

        monthly_expenses = (
            self.analytics.calculate_monthly_expenses()
        )

        monthly_budget = (
            self.budget_manager.get_monthly_budget()
        )

        report = []

        report.append(
            "=" * 55
        )

        report.append(
            "              MONTHLY EXPENSE REPORT"
        )

        report.append(
            "=" * 55
        )

        report.append("")

        report.append(
            f"Monthly Budget: ₹{monthly_budget:.2f}"
        )

        report.append("")

        for month, amount in monthly_expenses.items():

            report.append(
                f"{month}: ₹{amount:.2f}"
            )

        total = (
            self.analytics.calculate_total_expenses()
        )

        report.append("")

        report.append(
            f"Total Expenses: ₹{total:.2f}"
        )

        if monthly_budget > 0:

            remaining = monthly_budget - total

            usage = (
                total / monthly_budget
            ) * 100

            report.append(
                f"Remaining Budget: ₹{remaining:.2f}"
            )

            report.append(
                f"Budget Usage: {usage:.2f}%"
            )

        report.append("")

        report.append(
            "=" * 55
        )

        return "\n".join(report)

    def generate_category_report(self):
        """Generate category-wise expense report."""

        category_totals = (
            self.analytics.calculate_category_expenses()
        )

        percentages = (
            self.analytics.calculate_category_percentages()
        )

        report = []

        report.append(
            "=" * 55
        )

        report.append(
            "             CATEGORY EXPENSE REPORT"
        )

        report.append(
            "=" * 55
        )

        report.append("")

        for category, amount in category_totals.items():

            percentage = percentages.get(
                category,
                0
            )

            report.append(
                f"{category:<20}"
                f"₹{amount:>10.2f}   "
                f"{percentage:>6.2f}%"
            )

        report.append("")

        report.append(
            "=" * 55
        )

        return "\n".join(report)

    def generate_budget_report(self):
        """Generate budget status report."""

        monthly_budget = (
            self.budget_manager.get_monthly_budget()
        )

        category_budgets = (
            self.budget_manager.get_category_budgets()
        )

        total_spent = (
            self.analytics.calculate_total_expenses()
        )

        report = []

        report.append(
            "=" * 55
        )

        report.append(
            "               BUDGET REPORT"
        )

        report.append(
            "=" * 55
        )

        report.append("")

        report.append(
            f"Monthly Budget: ₹{monthly_budget:.2f}"
        )

        report.append(
            f"Total Spent: ₹{total_spent:.2f}"
        )

        if monthly_budget > 0:

            remaining = monthly_budget - total_spent

            usage = (
                total_spent / monthly_budget
            ) * 100

            report.append(
                f"Remaining: ₹{remaining:.2f}"
            )

            report.append(
                f"Usage: {usage:.2f}%"
            )

        report.append("")

        report.append(
            "Category Budgets:"
        )

        category_status = (
            self.analytics.get_category_budget_status(
                category_budgets
            )
        )

        for category, data in category_status.items():

            report.append(
                f"{category}: "
                f"Budget ₹{data['budget']:.2f}, "
                f"Spent ₹{data['spent']:.2f}, "
                f"Usage {data['usage']:.2f}%"
            )

        report.append("")

        report.append(
            "=" * 55
        )

        return "\n".join(report)

    def save_report(self, report, filename):
        """Save a text report."""

        file_path = os.path.join(
            self.output_directory,
            filename
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return file_path

    def export_category_csv(self):
        """Export category analytics to CSV."""

        category_totals = (
            self.analytics.calculate_category_expenses()
        )

        percentages = (
            self.analytics.calculate_category_percentages()
        )

        file_path = os.path.join(
            self.output_directory,
            "category_report.csv"
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Category",
                "Amount",
                "Percentage"
            ])

            for category, amount in category_totals.items():

                writer.writerow([
                    category,
                    f"{amount:.2f}",
                    f"{percentages[category]:.2f}"
                ])

        return file_path