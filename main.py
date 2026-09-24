def display_menu():
    print("\n" + "=" * 45)
    print("       SMART EXPENSE & BUDGET ANALYZER")
    print("=" * 45)
    print("1. Expense Management")
    print("2. Budget Management")
    print("3. Expense Analytics")
    print("4. Spending Insights")
    print("5. Generate Reports")
    print("6. Exit")
    print("=" * 45)


def main():
    print("Welcome to Smart Expense & Budget Analyzer!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Expense Management - Coming Soon")
            input("Press Enter to return to the main menu...")

        elif choice == "2":
            print("Budget Management - Coming Soon")
            input("Press Enter to return to the main menu...")

        elif choice == "3":
            print("Expense Analytics - Coming Soon")
            input("Press Enter to return to the main menu...")

        elif choice == "4":
            print("Spending Insights - Coming Soon")
            input("Press Enter to return to the main menu...")

        elif choice == "5":
            print("Report Generation - Coming Soon")
            input("Press Enter to return to the main menu...")

        elif choice == "6":
            print("Thank you for using Smart Expense & Budget Analyzer!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()