class Account:
        def __init__(self, balance=100):
            self.balance = balance

        def deposit(self, amount):
            if amount <= 0:
                return "Deposit amount cannot be less or equal to zero "
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount <= 0:
                return "Withdrawal amount cannot be less or equal to zero "
            if amount > self.balance:
                return "Insufficient funds"
            self.balance -= amount
            return f"Your balance remains {self.balance}"

        def get_balance(self):
            return f"Your account balance is {self.balance}"

PIN = 1234
your_pin = int(input("Enter your PIN: "))

if your_pin != PIN:
    exit("Incorrect PIN")

lammy = Account()
print(lammy.deposit(1000))
print(lammy.withdraw(10))
print(lammy.get_balance())