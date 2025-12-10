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

def login():
    pin = input("Enter PIN: ")
    if pin in users_data:
        print("Login Successful")
        return pin

    else:
        print("Login Failed: Invalid PIN")
        return None

def check_balance(pin):
    balance = users_data[pin]["balance"]
    print(f'Your current balance is {balance}\n')

    users_data[pin]["history"].append(f" Checked balance is : {balance}")

def deposit(pin):
    amount = (input("Enter amount to deposit: "))

    if not amount.isdigit():
        print("Invalid amount")
        return

    amount = int(amount)
    if amount <= 0:
        print("Deposit Failed: Invalid amount")
        return

    balance = users_data[pin]["balance"]
    balance += amount
    users_data[pin]["balance"] = balance

    print(f'You deposited {amount} ')
    users_data[pin]["history"].append(f" Deposited {amount} ")
    save_transactions()


def withdraw(pin):
    balance = users_data[pin]["balance"]
    amount = (input("Enter amount to withdraw: "))
    if not amount.isdigit():
        print("Invalid amount")
        return
    amount = int(amount)
    if amount <= 0:
        print("amount must be positive")
        return
    if amount > balance:
        print(f"Insufficient balance, you have {balance} in your account")
        return

    users_data[pin]["balance"] -= amount
    new_balance = users_data[pin]["balance"]
    print(f" Withdrawal succesfull {amount}, new balance is : {new_balance}")

    users_data[pin]["history"].append(f' Withdrawn {amount} ')
    save_transactions()

def transfer(pin):
    recipient = input("Enter recipient pin: ")
    if not recipient in users_data:
        print("Invalid recipient")
        return

    if recipient == pin:
        print("You can't transfer yourself")
        return
    amount = (input("Enter amount to transfer: "))
    if not amount.isdigit():
        print("Invalid amount")
        return
    amount = int(amount)
    if amount <= 0:
        print("amount must be positive")
        return
    if amount > users_data[pin]["balance"]:
        print(f" Insufficient balance, you have {users_data[pin]['balance']} ")
        return

    users_data[pin]["balance"] -= amount
    users_data[recipient]["balance"] += amount

    print(f'You transferred {amount} to {recipient}\n')
    users_data[pin]["history"].append(f' Transferred {amount} to {recipient}')
    users_data[recipient]["history"].append(f' Recieved {amount} from {pin}')
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

user = login()
if user:
    main_menu(user)