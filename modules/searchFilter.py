"""
Student Performance Analytics - Search and Filtering Extension

This module provides additional search/filter functionality for the V2 project.
It is an extension layer and does not replace the original analysis modules.
"""

import pandas as pd


def _print_results(results):
    """Print a compact table of matching students."""
    if results.empty:
        print("\nNo matching students found.")
        return

    display_columns = [
        col for col in [
            "roll_no", "name", "department",
            "attendance", "percentage", "grade", "result"
        ] if col in results.columns
    ]

    print(f"\nFound {len(results)} matching student(s):\n")
    print(results[display_columns].to_string(index=False))


def search_by_name(df):
    """Search students by a partial name match."""
    name = input("Enter student name (or part of the name): ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Case-insensitive partial matching.
    mask = df["name"].astype(str).str.contains(name, case=False, na=False)
    _print_results(df[mask])


def filter_by_department(df):
    """Filter students by department."""
    if "department" not in df.columns:
        print("Department information is not available.")
        return

    departments = sorted(df["department"].dropna().astype(str).unique())

    print("\nAvailable departments:")
    for department in departments:
        print(f"- {department}")

    department = input("Enter department: ").strip()

    if not department:
        print("Department cannot be empty.")
        return

    mask = df["department"].astype(str).str.casefold() == department.casefold()
    _print_results(df[mask])


def filter_by_percentage(df):
    """Show students whose percentage is at least the requested value."""
    value = input("Enter minimum percentage: ").strip()

    try:
        minimum = float(value)
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 0 <= minimum <= 100:
        print("Percentage must be between 0 and 100.")
        return

    mask = pd.to_numeric(df["percentage"], errors="coerce") >= minimum
    _print_results(df[mask].sort_values("percentage", ascending=False))


def filter_by_grade(df):
    """Filter students by grade."""
    grade = input("Enter grade (for example A+, A, B, C): ").strip()

    if not grade:
        print("Grade cannot be empty.")
        return

    mask = df["grade"].astype(str).str.casefold() == grade.casefold()
    _print_results(df[mask])


def filter_by_result(df):
    """Filter students by pass/fail result."""
    result = input("Enter result (Pass/Fail): ").strip()

    if result.casefold() not in {"pass", "fail"}:
        print("Please enter either Pass or Fail.")
        return

    mask = df["result"].astype(str).str.casefold() == result.casefold()
    _print_results(df[mask])


def search_filter_menu(df):
    """Interactive menu for the V2 search and filtering features."""
    while True:
        print("\n" + "=" * 50)
        print("SEARCH AND FILTER")
        print("=" * 50)
        print("1. Search by student name")
        print("2. Filter by department")
        print("3. Filter by minimum percentage")
        print("4. Filter by grade")
        print("5. Filter by result")
        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            search_by_name(df)
        elif choice == "2":
            filter_by_department(df)
        elif choice == "3":
            filter_by_percentage(df)
        elif choice == "4":
            filter_by_grade(df)
        elif choice == "5":
            filter_by_result(df)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
