class SpendingInsights:

    def __init__(self, analytics, budget_manager):
        self.analytics = analytics
        self.budget_manager = budget_manager

    def generate_insights(self):
        """Generate spending insights based on expenses and budgets."""

        insights = []

        expenses = self.analytics.expenses

        if not expenses:
            insights.append(
                "No expenses are available for analysis."
            )
            return insights

        # Total spending
        total = self.analytics.calculate_total_expenses()

        insights.append(
            f"Your total recorded spending is ₹{total:.2f}."
        )

        # Highest category
        top_category = self.analytics.find_top_category()

        if top_category:

            category_totals = (
                self.analytics.calculate_category_expenses()
            )

            top_amount = category_totals[top_category]

            insights.append(
                f"{top_category} is your highest "
                f"spending category with "
                f"₹{top_amount:.2f} spent."
            )

        # Category percentages
        percentages = (
            self.analytics.calculate_category_percentages()
        )

        for category, percentage in percentages.items():

            if percentage >= 40:

                insights.append(
                    f"{category} accounts for "
                    f"{percentage:.1f}% of your "
                    f"total spending."
                )

        # Large expenses
        large_expenses = (
            self.analytics.find_large_expenses(1000)
        )

        if large_expenses:

            insights.append(
                f"You have {len(large_expenses)} "
                f"expense(s) of ₹1,000 or more."
            )

        # Monthly budget
        monthly_budget = (
            self.budget_manager.get_monthly_budget()
        )

        if monthly_budget > 0:

            usage = (
                self.analytics.calculate_budget_usage(
                    monthly_budget
                )
            )

            if usage > 100:

                insights.append(
                    f"Your spending has exceeded "
                    f"the monthly budget by "
                    f"{usage - 100:.1f}%."
                )

            elif usage >= 80:

                insights.append(
                    f"You have used {usage:.1f}% "
                    f"of your monthly budget."
                )

            else:

                insights.append(
                    f"You have used {usage:.1f}% "
                    f"of your monthly budget."
                )

        # Category budgets
        category_budgets = (
            self.budget_manager.get_category_budgets()
        )

        if category_budgets:

            category_status = (
                self.analytics.get_category_budget_status(
                    category_budgets
                )
            )

            for category, data in category_status.items():

                if data["usage"] > 100:

                    insights.append(
                        f"{category} category has "
                        f"exceeded its budget by "
                        f"₹{abs(data['remaining']):.2f}."
                    )

                elif data["usage"] >= 80:

                    insights.append(
                        f"{category} category has used "
                        f"{data['usage']:.1f}% "
                        f"of its budget."
                    )

        return insights