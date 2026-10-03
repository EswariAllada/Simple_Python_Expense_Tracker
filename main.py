import json
import pandas as pd
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
print("================================")
print("        EXPENSE TRACKER")
print("================================")
print()
print("Welcome to your Expense Tracker!")

while True:
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount}
        expenses.append(expense)
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("Expense added successfully!")
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            df = pd.DataFrame(expenses)
            print(df)
    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
            print("Total Expenses: ₹", total)
    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(i, ".", expense["date"], "-", expense["description"])
            number = int(input("Enter expense number to delete: "))
            if 1 <= number <= len(expenses):
                deleted_expense = expenses.pop(number - 1)
                with open("expenses.json", "w") as file:
                    json.dump(expenses, file, indent=4)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number.")
    elif choice == '5':
        print("Thank you")
        break
    else:
        print("Invalid choice!")