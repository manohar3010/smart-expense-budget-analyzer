from datetime import datetime


def generate_expense_id(expenses):
    """Generate a unique expense ID."""
    if not expenses:
        return "E001"

    numbers = []

    for expense in expenses:
        expense_id = expense.get("expense_id", "")

        if expense_id.startswith("E"):
            try:
                numbers.append(int(expense_id[1:]))
            except ValueError:
                continue

    next_number = max(numbers, default=0) + 1

    return f"E{next_number:03d}"


def get_current_date():
    """Return today's date in DD-MM-YYYY format."""
    return datetime.now().strftime("%d-%m-%Y")