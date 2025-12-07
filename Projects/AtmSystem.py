
menu = ('\n Click any of the options below to get started.'
        '\n 1. Check balance'
        '   2. Deposit '
        '   3. Withdraw'
        '   4. View Transaction history'
        '   5. Tranfer Money'
        '   6. exit')


class Account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        return f" You deposited {amount}, new balance is {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.balance:
            return "Insufficient funds"

        self.balance -= amount
        return f" You withdrew {amount}, your new balance is {self.balance}"

    def get_balance(self):
        return f"Your account balance is {self.balance}"

    def print_history(self):
        if not self.history:
            return "No transactions yet"
        return "\n".join(self.history)

account_data = {
    '1234': Account('edu', '1234', 100),
    '2345': Account('basit', '2345', 100),
    '3456': Account('khalid', '3456', 100),
    '4567': Account('habeeb', '4567', 100),
    '5678': Account('Lukmon', '5678', 100),
}

input_pin = input("Enter PIN: ")


if input_pin not in account_data:
    print("Incorrect PIN, please try again")
    exit()

user = account_data[input_pin]
print(f"welcome {user.name}")

print(menu)
choice = input('Enter your choice: ')

while True:
    if choice == '1':
        print(user.get_balance())

    elif choice == '2':
        user_deposit = float(input("enter amount to deposit: "))
        print(user.deposit(user_deposit))

    elif choice == '3':
        user_withdraw = float(input("enter amount to withdraw: "))
        print(user.withdraw(user_withdraw))
        break

    elif choice == '4':
        print(user.print_history())
        break

    elif choice == '5':
        reciever_pin = input("Enter reciever pin: ")

        if reciever_pin not in account_data:
            print("Incorrect PIN, please try again")
            continue
        else:
            transferred_amount = float(input("enter amount to transfer: "))
            reciever = account_data[reciever_pin]

            if transferred_amount < 0:
                print("Amount must be positive")
                continue

            elif transferred_amount > user.balance:
                print("Insufficient funds")
                break

            user.balance -= transferred_amount
            reciever.balance += transferred_amount

            user.history.append(f" You've transferred {transferred_amount} to {reciever.name}")
            reciever.history.append(f" You've recieved {transferred_amount} from {user.name}")

            print(f" Transfer of {transferred_amount} to {reciever.name} ")

    elif choice == '6':
        print("Thanks for using our services")
        exit()

    else:
        print("Invalid choice, please try again")
