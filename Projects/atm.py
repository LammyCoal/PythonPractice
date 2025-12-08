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
    pass

def deposit(pin):
    pass

def withdraw(pin):
    pass

def transfer(pin):
    pass

def view_history():
    pass

def save_transactions():
    pass

def main_menu():

    while True:
            menu = ('\n Click any of the options below to get started.'
                    '\n 1. Check balance'
                    '   2. Deposit '
                    '   3. Withdraw'
                    '   4. View Transaction history'
                    '   5. Transfer Money'
                    '   6. exit')
            print(menu)