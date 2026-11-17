# Personal Expense Tracker

## Project Details
- *Project Number:* 04
- *Language:* Python 3
- *Developer:* Adarsh mishra
- *ERP:* RU-26-02492

## Project Mentor
- *Mentored by:* Mr. Satyaprakash Sethy (https://github.com/SATYAPRAKASHSETHY)
- *Github:* @SATYAPRAKASHSETHY(https://github.com/SATYAPRAKASHSETHY)
- *Role:* Python Mentor/ Technical Guide

## 1. Introduction

The Personal Expense Tracker is a menu-driven Python application that helps users record and review their daily expenses. It stores expense records in a CSV file and uses the Pandas library to display category-wise and monthly spending summaries.

## 2. Features

- Add an expense with date, category, description, and amount.
- Validate dates in `YYYY-MM-DD` format.
- Accept only positive numeric amounts.
- Prevent saving an expense when the category or description is empty.
- Store expense records in `expenses.csv`.
- View all saved expenses and total spending.
- Display category-wise expense summaries.
- Display monthly expense summaries.
- Keep saved records available when the application is restarted.

## 3. Requirements

- Python 3
- Pandas library

## 4. Installation

Install Pandas using:

```bash
pip install pandas
```

## 5. Project Structure

```text
Personal Expense Tracker/
├── expense_tracker.py
├── expenses.csv       # Created automatically when expenses are saved
└── README.md
```

## 6. How to Run

1. Save the Python source code as `expense_tracker.py`.
2. Open a terminal or command prompt in the project folder.
3. Install Pandas if it is not already installed.
4. Run the application:

```bash
python expense_tracker.py
```

## 7. Application Menu

When the program starts, it displays the following menu:

```text
PERSONAL EXPENSE TRACKER

1. Add Expense
2. View All Expenses
3. Category-wise Summary
4. Monthly Expense Summary
5. Exit
```

Enter a menu number to select an operation.

## 8. CSV Data Storage

The application stores records in `expenses.csv` with these columns:

| Column | Description |
|---|---|
| Date | Expense date in `YYYY-MM-DD` format |
| Category | Expense category, such as Food or Travel |
| Description | Short details about the expense |
| Amount | Positive numeric expense amount |

The CSV file is created automatically when the first valid expense is saved. Keep this file in the same folder as `expense_tracker.py` so the application can load saved records.

## 9. Validation

- Dates must be valid and follow `YYYY-MM-DD`.
- Amounts must be numeric and greater than zero.
- Category cannot be empty.
- Description cannot be empty.
- Invalid menu choices are rejected and the menu is displayed again.

## 10. Testing

The project can be tested by adding valid expenses, entering invalid dates and amounts, checking empty fields, viewing saved records, and verifying category-wise and monthly totals. Refer to the accompanying **Personal Expense Tracker Test Cases** document for detailed test scenarios and expected results.

## 11. Limitations

- This is a local, single-user command-line application.
- Records are stored in a CSV file; there is no database or login system.
- The CSV file should not be manually edited with inconsistent column names or data formats.

## 12. Conclusion

The Personal Expense Tracker demonstrates the use of Python functions, input validation, file handling, and Pandas DataFrames for basic expense management. It provides a simple way to save expenses and review spending patterns by category and month.
