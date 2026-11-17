"""
Personal Expense Tracker
Project: PS No. 4
Language: Python 3

Requirements:
- Add expenses with date, category, description and amount.
- Store records in expenses.csv.
- View all saved expenses.
- Display category-wise and monthly summaries using Pandas.
- Validate date format and positive amount before saving.

Install Pandas if needed:
    pip install pandas
"""

import os
import pandas as pd
from datetime import datetime

CSV_FILE = "expenses.csv"
COLUMNS = ["Date", "Category", "Description", "Amount"]


def load_expenses():
    """Load saved expenses, or create an empty DataFrame."""
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=COLUMNS)

    try:
        data = pd.read_csv(CSV_FILE)
        # Ensure the CSV has the required columns.
        for column in COLUMNS:
            if column not in data.columns:
                data[column] = ""
        data = data[COLUMNS]
        data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
        data = data.dropna(subset=["Amount"])
        return data
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=COLUMNS)


def save_expenses(data):
    """Save all expense records to the CSV file."""
    data.to_csv(CSV_FILE, index=False)


def get_valid_date():
    """Accept only dates in YYYY-MM-DD format."""
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            parsed_date = datetime.strptime(date_text, "%Y-%m-%d")
            if parsed_date.strftime("%Y-%m-%d") != date_text:
                raise ValueError
            return date_text
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD (example: 2026-08-10).")


def get_valid_amount():
    """Accept only a positive numeric amount."""
    while True:
        amount_text = input("Enter amount: ").strip()
        try:
            amount = float(amount_text)
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number. Expense not saved.")
                return None
            return amount
        except ValueError:
            print("Invalid amount. Please enter a positive number.")


def add_expense():
    """Take expense details and append a valid record to the CSV."""
    data = load_expenses()

    date = get_valid_date()
    category = input("Enter category (e.g. Food, Travel): ").strip()
    if not category:
        print("Category cannot be empty. Expense not saved.")
        return

    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty. Expense not saved.")
        return

    amount = get_valid_amount()
    if amount is None:
        return

    new_expense = pd.DataFrame(
        [[date, category.title(), description, amount]],
        columns=COLUMNS
    )
    data = pd.concat([data, new_expense], ignore_index=True)
    save_expenses(data)

    print(f"\nExpense saved. Total records: {len(data)}")


def view_expenses():
    """Display every saved expense."""
    data = load_expenses()

    if data.empty:
        print("\nNo expenses found.")
        return

    print("\nALL EXPENSES")
    print("-" * 75)
    display_data = data.copy()
    display_data["Amount"] = display_data["Amount"].map(lambda value: f"{value:g}")
    print(display_data.to_string(index=False))
    print("-" * 75)
    print(f"Total spending: {data['Amount'].sum():g}")


def category_summary():
    """Display total spending for each category using Pandas groupby()."""
    data = load_expenses()

    if data.empty:
        print("\nNo expenses available for summary.")
        return

    summary = data.groupby("Category")["Amount"].sum().reset_index()
    print("\nCATEGORY-WISE SUMMARY")
    print("-" * 35)
    for _, row in summary.iterrows():
        print(f"{row['Category']}: {row['Amount']:g}")
    print("-" * 35)
    print(f"Total: {data['Amount'].sum():g}")


def monthly_summary():
    """Display total spending month-wise."""
    data = load_expenses()

    if data.empty:
        print("\nNo expenses available for summary.")
        return

    dates = pd.to_datetime(data["Date"], format="%Y-%m-%d", errors="coerce")
    valid_data = data.loc[dates.notna()].copy()
    valid_data["Month"] = dates[dates.notna()].dt.strftime("%B %Y")

    summary = valid_data.groupby("Month")["Amount"].sum()
    print("\nMONTHLY EXPENSE SUMMARY")
    print("-" * 35)
    for month, amount in summary.items():
        print(f"{month}: {amount:g}")
    print("-" * 35)
    print(f"Total: {valid_data['Amount'].sum():g}")


def main():
    """Main menu of the Personal Expense Tracker."""
    while True:
        print("\n" + "=" * 40)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Monthly Expense Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
