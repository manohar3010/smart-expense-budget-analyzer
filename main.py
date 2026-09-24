from src.expense_manager import ExpenseManager


expense_manager = ExpenseManager()


def display_menu():
    print("\n" + "=" * 50)
    print("       SMART EXPENSE & BUDGET ANALYZER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Filter by Category")
    print("7. Budget Management")
    print("8. Expense Analytics")
    print("9. Spending Insights")
    print("10. Generate Report")
    print("11. Exit")
    print("=" * 50)


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
            print("\nBudget Management will be added on Day 3.")

        elif choice == "8":
            print("\nExpense Analytics will be added on Day 3.")

        elif choice == "9":
            print("\nSpending Insights will be added on Day 4.")

        elif choice == "10":
            print("\nReport Generation will be added on Day 4.")

        elif choice == "11":
            print("\nThank you for using Smart Expense & Budget Analyzer!")
            break

        else:
            print("\n✗ Invalid choice. Please select 1-11.")


if __name__ == "__main__":
    main()