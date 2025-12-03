expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": desc
    }

    expenses.append(expense)
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return

    print("\n--- All Expenses ---")
    total = 0
    for i, e in enumerate(expenses,start=1):
        print(f"{i}. {e['date']} | {e['category']} | ₹{e['amount']} | {e['description']}")
        total += e['amount']
    print("Total Spent:", total, "\n")

def summary_by_category():
    if not expenses:
        print("No expenses yet.\n")
        return

    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    print("\n--- Category Summary ---")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")
    print()

def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice!\n")

menu()
