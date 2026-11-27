import csv
expenses = []

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")

    try:
        amount = float(input("Amount: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    expenses.append([date, category, amount])
    print("Expense added.\n")


def import_csv():
    filename = input("Enter CSV filename: ")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                expenses.append([row[0], row[1], float(row[2])])

        print("Expenses imported.\n")

    except FileNotFoundError:
        print("File not found.\n")

def export_csv():
    filename = input("Enter export filename: ")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])
        writer.writerows(expenses)

    print("Expenses exported.\n")

def monthly_report():
    monthly = {}

    for expense in expenses:
        month = expense[0][:7]  # YYYY-MM
        amount = expense[2]

        if month in monthly:
            monthly[month] += amount
        else:
            monthly[month] = amount

    print("\nMonthly Spending")
    for month in monthly:
        print(month, ":", monthly[month])


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Import CSV")
    print("3. Export CSV")
    print("4. Monthly Analytics")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        import_csv()

    elif choice == "3":
        export_csv()

    elif choice == "4":
        monthly_report()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")