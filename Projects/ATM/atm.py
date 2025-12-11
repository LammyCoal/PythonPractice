import json
import os

filename = 'users_data.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        users_data = json.load(f)
else:
    users_data ={
        "1234": {"balance": 1000, "history": []},
        "2345": {"balance": 2000, "history": []},
        "3456": {"balance": 2500, "history": []},
        "4567": {"balance": 3000, "history": []}
}
def create_account():
    pin = input("Enter a 4-digit pin: ")
    if pin in users_data:
        print("pin already exists")
        return

    if not pin.isdigit() or len(pin) != 4:
        print("pin must be 4 digits")
        return

    confirm = input("Re-enter pin: ")
    if confirm != pin:
        print("pin doesn't match")
        return

    name = input("Enter your name: ")
    users_data[pin] = {
        "name": name,
        "balance": 0,
        "history": []

    }

    print(f'Account created successfully {name}')
    save_transactions()


def login():
    pin = input("Enter PIN: ")
    if pin in users_data:
        print(f"Login Successful, welcome {users_data[pin]['name']}")
        return pin

    else:
        print("Login Failed: Invalid PIN")
        return None


def convert_to_num(value):
    try:
        float(value)
        return True
    except:
        return False

def check_balance(pin):
    balance = users_data[pin]["balance"]
    print(f'Your current balance is ₦{format(balance, ',')}')

    users_data[pin]["history"].append(f" Checked balance is : ₦{format(balance, ',')}")


def deposit(pin):
    amount = (input("Enter amount to deposit: "))

    if not convert_to_num(amount):
        print("Incorrect amount")
        return

    amount = float(amount)
    if amount <= 0:
        print("Deposit Failed: Amount must be positive")
        return

    balance = users_data[pin]["balance"]
    balance += amount
    users_data[pin]["balance"] = balance

    print(f'You deposited {amount} ')
    users_data[pin]["history"].append(f" Deposited ₦{format(amount, ',')} ")
    save_transactions()


def withdraw(pin):
    balance = users_data[pin]["balance"]
    amount = (input("Enter amount to withdraw: "))

    if not convert_to_num(amount):
        print("Invalid input")
        return

    amount = float(amount)
    if amount <= 0:
        print("amount must be positive")
        return
    if amount > balance:
        print(f"Insufficient balance, you have ₦{format(balance, ',')} in your account")
        return

    users_data[pin]["balance"] -= amount
    new_balance = users_data[pin]["balance"]
    print(f" Withdrawal succesfull ₦{format(amount, ',')}, new balance is : ₦{format(new_balance, ',')}")

    users_data[pin]["history"].append(f' Withdrawn ₦{format(amount, ',')} ')
    save_transactions()


def transfer(pin):
    recipient = input("Enter recipient pin: ")
    if not recipient in users_data:
        print("Invalid recipient")
        return

    if recipient == pin:
        print("You can't transfer to yourself")
        return
    amount = (input("Enter amount to transfer: "))

    if not convert_to_num(amount):
        print("Invalid input")
        return

    amount = float(amount)
    if amount <= 0:
        print("amount must be positive")
        return

    if amount > users_data[pin]["balance"]:
        print(f" Insufficient balance, you have ₦{format(users_data[pin]['balance'],',')} ")
        return

    users_data[pin]["balance"] -= amount
    users_data[recipient]["balance"] += amount

    print(f'You transferred {format(amount, ',')} to {users_data[recipient]['name']}\n')
    users_data[pin]["history"].append(f' Transferred ₦{format(amount, ',')} to {users_data[recipient]['name']}')
    users_data[recipient]["history"].append(f' Recieved ₦{format(amount, ',')} from {users_data[pin]['name']}')
    save_transactions()

def view_history(pin):
    history = users_data[pin]["history"]

    if not history:
        print("No history")
        return

    print("----Transaction History----\n")
    for i, transaction in enumerate(history, 1):
        print(f"{i}. {transaction}")
    print()


def save_transactions():
    with open(filename, 'w') as f:
        json.dump(users_data, f, indent=4)


def main_menu(pin):
    while True:
        menu = ('\n Click any of the options below to get started.'
                '\n 1. Check balance'
                '   2. Deposit '
                '   3. Withdraw'
                '   4. View Transaction history'
                '   5. Transfer Money'
                '   6. exit')
        print(menu)

        choice = input('Enter your choice: ')

        if choice == '1':
            check_balance(pin)
        elif choice == '2':
            deposit(pin)
        elif choice == '3':
            withdraw(pin)
        elif choice == '4':
            view_history(pin)
        elif choice == '5':
            transfer(pin)
        elif choice == '6':
            save_transactions()
            print("Thanks for using ATM")
            break
        else:
            print("Invalid Choice")

# main menu
while True:
    print("""
    1. login
    2. create account
    3. Exit
    """)
    choice = input('Enter your choice: ')
    if choice == '1':
        user = login()
        if user:
            main_menu(user)

    elif choice == '2':
        create_account()

    elif choice == '3':
        print("Goodbye")
        break

    else:
        print("Invalid Input")