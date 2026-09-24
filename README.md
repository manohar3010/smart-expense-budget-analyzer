# Smart Expense & Budget Analyzer

## 1. Project Overview

Smart Expense & Budget Analyzer is a Python-based command-line application designed to help users record, manage, analyze, and monitor their personal expenses.

The application allows users to maintain expense records, categorize transactions, set monthly and category-wise budgets, analyze spending patterns, generate spending insights, and create financial reports.

The project demonstrates modular Python programming, file handling, data processing, input validation, exception handling, automated testing, and Git-based version control.

---

## 2. Problem Statement

Students and individuals often find it difficult to track their daily expenses and understand their spending patterns. Expenses may be recorded manually or not tracked consistently, making it difficult to monitor budgets, identify major spending categories, and plan expenses effectively.

The Smart Expense & Budget Analyzer provides a command-line solution for recording expenses, managing budgets, analyzing spending patterns, generating insights, and producing financial reports.

---

## 3. Objectives

* Develop a Python-based personal expense management application.
* Allow users to add, view, update, delete, search, and filter expenses.
* Provide monthly and category-wise budget management.
* Calculate spending statistics and category-wise expenditure.
* Identify major spending categories and large expenses.
* Provide spending insights based on recorded data.
* Generate monthly, category-wise, and budget reports.
* Implement input validation and error handling.
* Store data using CSV and JSON files.
* Demonstrate modular programming and automated testing.

---

## 4. Features

### 4.1 Expense Management

* Add new expenses
* View all expenses
* Update existing expenses
* Delete expenses
* Search expenses
* Filter expenses by category
* Store expenses in CSV format

### 4.2 Budget Management

* Set monthly budget
* Set category-wise budgets
* View configured budgets
* View budget utilization
* Calculate remaining budget
* Detect budget overuse

### 4.3 Expense Analytics

* Calculate total expenses
* Calculate category-wise expenses
* Calculate monthly expenses
* Calculate average spending per recorded day
* Identify highest individual expense
* Identify highest spending category
* Calculate category spending percentages
* Identify large expenses
* Compare budget utilization

### 4.4 Spending Insights

The system generates textual insights based on:

* Total spending
* Highest spending category
* Category spending percentages
* Large expenses
* Monthly budget usage
* Category budget usage

### 4.5 Report Generation

The system generates:

* Monthly expense report
* Category expense report
* Budget report
* Category-wise CSV report

---

## 5. Technology Stack

| Technology             | Purpose                 |
| ---------------------- | ----------------------- |
| Python 3               | Application development |
| CSV                    | Expense data storage    |
| JSON                   | Budget data storage     |
| unittest               | Automated testing       |
| Git                    | Version control         |
| GitHub                 | Source code hosting     |
| VS Code                | Development environment |
| Command Line Interface | User interaction        |

The project uses Python standard-library modules and does not require external Python packages for the core application.

---

## 6. Project Architecture

The application follows a modular architecture.

```text
                    ┌─────────────────────┐
                    │      main.py        │
                    │   CLI Interface     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │   Expense   │  │   Budget    │  │  Analytics  │
       │   Manager   │  │   Manager   │  │   Module    │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              ▼                ▼                ▼
       expenses.csv       budget.json      Calculations
                                                │
                         ┌──────────────────────┤
                         │                      │
                         ▼                      ▼
                  ┌─────────────┐       ┌───────────────┐
                  │   Spending  │       │    Report     │
                  │   Insights  │       │   Generator   │
                  └─────────────┘       └───────────────┘
```

---

## 7. Project Structure

```text
smart-expense-budget-analyzer/
│
├── main.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── expenses.csv
│   └── budget.json
│
├── src/
│   ├── __init__.py
│   ├── expense_manager.py
│   ├── budget_manager.py
│   ├── analytics.py
│   ├── insights.py
│   ├── report_generator.py
│   ├── validator.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_expense.py
│   ├── test_budget.py
│   └── test_analytics.py
│
├── reports/
│
└── docs/
```

---

## 8. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/manohar3010/smart-expense-budget-analyzer.git
```

### Step 2: Open the project

```bash
cd smart-expense-budget-analyzer
```

### Step 3: Create a virtual environment

Windows:

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Command Prompt:

```bash
venv\Scripts\activate
```

---

## 9. Running the Application

Run the following command from the project root:

```bash
python main.py
```

The application displays a command-line menu containing options for:

* Expense Management
* Budget Management
* Analytics
* Spending Insights
* Reports

---

## 10. Running Tests

The project uses Python's built-in `unittest` framework.

Run:

```bash
python -m unittest discover -s tests -v
```

A successful test run should display all tests as `ok` and finish with:

```text
OK
```

---

## 11. Data Storage

### Expenses

Expense records are stored in:

```text
data/expenses.csv
```

The CSV contains:

```text
expense_id
date
category
amount
description
payment_method
```

### Budgets

Budget information is stored in:

```text
data/budget.json
```

The file stores:

* Monthly budget
* Category-wise budgets

---

## 12. Input Validation

The application validates:

* Expense amount
* Date format
* Expense category
* Payment method
* Expense description
* Budget values

Invalid inputs are rejected with appropriate messages instead of being processed as valid records.

---

## 13. Reports

Generated reports are stored inside:

```text
reports/
```

Available reports include:

```text
monthly_report.txt
category_report.txt
budget_report.txt
category_report.csv
```

---

## 14. Testing

The project includes automated tests for important functionality.

Tested areas include:

* Adding expenses
* Invalid expense amounts
* Total expense calculation
* Highest spending category
* Category percentage calculation

Manual testing was also performed for:

* Expense CRUD operations
* Search and filtering
* Budget management
* Analytics
* Spending insights
* Report generation
* Invalid user inputs

---

## 15. Error Handling

The application handles invalid user inputs such as:

* Negative amounts
* Non-numeric amounts
* Invalid dates
* Invalid categories
* Invalid payment methods
* Invalid budget values

The system displays meaningful error messages and prevents invalid data from being stored.

---

## 16. Future Enhancements

Possible future improvements include:

* Graphical user interface
* Database integration using SQLite
* User authentication
* Advanced spending visualizations
* Monthly spending trend charts
* Recurring expense support
* Export to PDF
* Personalized financial recommendations
* Optional AI-assisted spending summaries

---

## 17. Learning Outcomes

Through this project, the following concepts were applied:

* Python functions
* Classes and objects
* Modular programming
* File handling
* CSV processing
* JSON processing
* Exception and input handling
* Data processing
* Automated testing
* Git and GitHub
* Command-line application development

---

## 18. Conclusion

Smart Expense & Budget Analyzer provides a structured command-line solution for personal expense and budget management.

The project combines expense management, budgeting, analytics, spending insights, and report generation into a modular Python application while demonstrating practical software development concepts such as validation, file handling, testing, documentation, and version control.
