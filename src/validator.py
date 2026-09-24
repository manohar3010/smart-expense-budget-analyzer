from datetime import datetime


VALID_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Education",
    "Entertainment",
    "Health",
    "Other"
]

VALID_PAYMENT_METHODS = [
    "UPI",
    "Cash",
    "Card",
    "Bank Transfer"
]


def validate_amount(amount):
    """Validate whether the amount is a positive number."""
    try:
        amount = float(amount)

        if amount <= 0:
            return False, "Amount must be greater than zero."

        return True, ""

    except ValueError:
        return False, "Amount must be a valid number."


def validate_date(date):
    """Validate date in DD-MM-YYYY format."""
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True, ""

    except ValueError:
        return False, "Date must be in DD-MM-YYYY format."


def validate_category(category):
    """Validate expense category."""
    if category.title() not in VALID_CATEGORIES:
        return False, (
            "Invalid category. Choose from: "
            + ", ".join(VALID_CATEGORIES)
        )

    return True, ""


def validate_payment_method(payment_method):
    """Validate payment method."""
    if payment_method.title() not in VALID_PAYMENT_METHODS:
        return False, (
            "Invalid payment method. Choose from: "
            + ", ".join(VALID_PAYMENT_METHODS)
        )

    return True, ""