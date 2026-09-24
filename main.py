from src.expense_manager import ExpenseManager
from src.budget_manager import BudgetManager
from src.analytics import ExpenseAnalytics

expense_manager = ExpenseManager()
budget_manager = BudgetManager()
analytics = ExpenseAnalytics(expense_manager.view_expenses())

def display_menu():
    print("\n" + "=" * 55)
    print("        SMART EXPENSE & BUDGET ANALYZER")
    print("=" * 55)

    print("\nEXPENSE MANAGEMENT")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Filter by Category")

    print("\nBUDGET MANAGEMENT")
    print("7. Set Monthly Budget")
    print("8. Set Category Budget")
    print("9. View Budget")
    print("10. View Budget Status")

    print("\nANALYTICS")
    print("11. View Expense Analytics")

    print("\nOTHER")
    print("12. Spending Insights")
    print("13. Generate Report")
    print("14. Exit")

    print("=" * 55)



def add_expense():
    print("\n--- ADD EXPENSE ---")

    date = input("Enter date (DD-MM-YYYY): ").strip()
    category = input("Enter category: ").strip()
    amount = input("Enter amount: ").strip()
    description = input("Enter description: ").strip()
    payment_method = input("Enter payment method: ").strip()

    success, result = expense_manager.add_expense(
        date,
        category,
        amount,
        description,
        payment_method
    )

    if success:
        print(f"\n✓ Expense added successfully.")
        print(f"Expense ID: {result}")
    else:
        print(f"\n✗ {result}")


def view_expenses():
    print("\n--- ALL EXPENSES ---")

    expenses = expense_manager.view_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 90)

    print(
        f"{'ID':<8}"
        f"{'Date':<14}"
        f"{'Category':<18}"
        f"{'Amount':<12}"
        f"{'Description':<20}"
        f"{'Payment':<15}"
    )

    print("-" * 90)

    for expense in expenses:

        print(
            f"{expense['expense_id']:<8}"
            f"{expense['date']:<14}"
            f"{expense['category']:<18}"
            f"₹{expense['amount']:<11}"
            f"{expense['description']:<20}"
            f"{expense['payment_method']:<15}"
        )

    print("-" * 90)


def update_expense():
    print("\n--- UPDATE EXPENSE ---")

    expense_id = input("Enter expense ID: ").strip()

    expense = expense_manager.find_expense(expense_id)

    if expense is None:
        print("✗ Expense not found.")
        return

    print("\nEnter new details.")

    date = input(f"Date [{expense['date']}]: ").strip()
    category = input(
        f"Category [{expense['category']}]: "
    ).strip()

    amount = input(
        f"Amount [{expense['amount']}]: "
    ).strip()

    description = input(
        f"Description [{expense['description']}]: "
    ).strip()

    payment_method = input(
        f"Payment Method [{expense['payment_method']}]: "
    ).strip()

    date = date or expense["date"]
    category = category or expense["category"]
    amount = amount or expense["amount"]
    description = description or expense["description"]
    payment_method = payment_method or expense["payment_method"]

    success, message = expense_manager.update_expense(
        expense_id,
        date,
        category,
        amount,
        description,
        payment_method
    )

    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")


def delete_expense():
    print("\n--- DELETE EXPENSE ---")

    expense_id = input("Enter expense ID: ").strip()

    expense = expense_manager.find_expense(expense_id)

    if expense is None:
        print("✗ Expense not found.")
        return

    print("\nExpense details:")
    print(expense)

    confirmation = input(
        "Are you sure you want to delete this expense? (y/n): "
    ).lower()

    if confirmation == "y":

        success, result = expense_manager.delete_expense(expense_id)

        if success:
            print("✓ Expense deleted successfully.")
        else:
            print(f"✗ {result}")

    else:
        print("Deletion cancelled.")


def search_expenses():
    print("\n--- SEARCH EXPENSES ---")

    keyword = input(
        "Enter description or category to search: "
    ).strip()

    results = expense_manager.search_expenses(keyword)

    if not results:
        print("No matching expenses found.")
        return

    for expense in results:
        print(
            f"{expense['expense_id']} | "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )


def filter_expenses():
    print("\n--- FILTER BY CATEGORY ---")

    category = input("Enter category: ").strip()

    results = expense_manager.filter_by_category(category)

    if not results:
        print("No expenses found in this category.")
        return

    for expense in results:
        print(
            f"{expense['expense_id']} | "
            f"{expense['date']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )

def set_monthly_budget():
    print("\n--- SET MONTHLY BUDGET ---")

    amount = input("Enter monthly budget: ₹").strip()

    success, message = budget_manager.set_monthly_budget(amount)

    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")

def set_category_budget():
    print("\n--- SET CATEGORY BUDGET ---")

    category = input("Enter category: ").strip()
    amount = input("Enter category budget: ₹").strip()

    success, message = budget_manager.set_category_budget(
        category,
        amount
    )

    if success:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")

def view_budget():
    print("\n--- BUDGET INFORMATION ---")

    monthly_budget = budget_manager.get_monthly_budget()

    category_budgets = budget_manager.get_category_budgets()

    print(f"\nMonthly Budget: ₹{monthly_budget:.2f}")

    print("\nCategory Budgets:")

    if not category_budgets:
        print("No category budgets set.")
        return

    for category, amount in category_budgets.items():
        print(f"{category}: ₹{amount:.2f}")

def view_budget_status():
    print("\n--- BUDGET STATUS ---")

    expenses = expense_manager.view_expenses()

    analytics = ExpenseAnalytics(expenses)

    total_spent = analytics.calculate_total_expenses()

    monthly_budget = budget_manager.get_monthly_budget()

    if monthly_budget <= 0:
        print("No monthly budget has been set.")
        return

    remaining = monthly_budget - total_spent

    usage = analytics.calculate_budget_usage(
        monthly_budget
    )

    print(f"\nMonthly Budget : ₹{monthly_budget:.2f}")
    print(f"Total Spent    : ₹{total_spent:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")
    print(f"Budget Used    : {usage:.2f}%")

    if remaining < 0:
        print("\n⚠ Budget exceeded!")

    elif usage >= 80:
        print("\n⚠ You have used more than 80% of your budget.")

    else:
        print("\n✓ You are within your budget.")

def view_analytics():
    print("\n--- EXPENSE ANALYTICS ---")

    expenses = expense_manager.view_expenses()

    if not expenses:
        print("No expenses available for analysis.")
        return

    analytics = ExpenseAnalytics(expenses)

    total = analytics.calculate_total_expenses()

    category_totals = analytics.calculate_category_expenses()

    monthly_totals = analytics.calculate_monthly_expenses()

    average_daily = analytics.calculate_average_daily_expense()

    highest = analytics.find_highest_expense()

    top_category = analytics.find_top_category()

    print(f"\nTotal Expenses: ₹{total:.2f}")

    print("\nCategory-wise Expenses:")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

    print("\nMonthly Expenses:")

    for month, amount in monthly_totals.items():
        print(f"{month}: ₹{amount:.2f}")

    print(
        f"\nAverage Daily Expense: "
        f"₹{average_daily:.2f}"
    )

    if highest:
        print(
            "\nHighest Individual Expense:"
        )

        print(
            f"{highest['description']} - "
            f"₹{float(highest['amount']):.2f}"
        )

    if top_category:
        print(
            f"\nHighest Spending Category: "
            f"{top_category}"
        )

def main():

    print("\nWelcome to Smart Expense & Budget Analyzer!")

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_expenses()

        elif choice == "6":
            filter_expenses()

        elif choice == "7":
            set_monthly_budget()

        elif choice == "8":
            set_category_budget()

        elif choice == "9":
            view_budget()

        elif choice == "10":
            view_budget_status()

        elif choice == "11":
            view_analytics()

        elif choice == "12":
            print("\nSpending Insights will be added on Day 4.")

        elif choice == "13":
            print("\nReport Generation will be added on Day 4.")

        elif choice == "14":
            print(
                "\nThank you for using "
                "Smart Expense & Budget Analyzer!"
            )
            break
        else:
            print("\n Invalid choice. Please select 1-14.")
            
        

if __name__ == "__main__":
    main()