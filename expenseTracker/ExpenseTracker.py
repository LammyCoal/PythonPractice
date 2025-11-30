expenses = []
def add_expense():
    name = input("Enter expense: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print(f"{name} added to expense as: ₦{amount}")
    return

def view_expense():
    if not expenses:
        print("No expenses found")
        return
    print('\n Your expenses are:')
    for i, (name, amount) in enumerate(expenses, 1):
        print(f"{i}. {name}: ₦{amount}")

def total_expenses():
    total = sum(amount for (name, amount) in expenses)
    return f'\n Your total expense is: ₦{total}'

def save_expenses():
    if not expenses:
        print("No expenses found")
        return

    with open('expenses.txt', 'w', encoding='utf-8') as file:
        file.write("\n Your expenses are:")
        for i, (name, amount) in enumerate(expenses, 1):
            file.write(f"\n {i} {name}: ₦{amount}")
        file.write(f'\n Total = ₦{sum(amount for _, amount in expenses)}')

add_expense()
add_expense()
print(total_expenses())
view_expense()
save_expenses()