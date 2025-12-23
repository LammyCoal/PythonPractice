class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def student_id(self):
        print(f'Student ID: {self.name}, Age: {self.age}')


lammy = Student('Lammy', 22)
lammy.student_id()

class BankAccount:
    bank_name = "Zenith Bank"
    account_size = 7


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 120
        BankAccount.change_size()

    def balance(self):
        print(f'Bank ID: {self.name}, Balance: {self.balance}')

    @classmethod
    def change_name(cls, new_name, open_account):
        cls.bank_name = new_name
        cls.open_account = open_account

    @classmethod
    def change_size(cls):
        cls.account_size += 5

    @staticmethod
    def show_bank_name():
        return BankAccount.bank_name

    @staticmethod
    def add_money(amount):
        return f'{amount} added to account'

lammycoal = BankAccount('Lammy', 22)
edu = BankAccount('Edu', 23)



BankAccount.open_account = 23
print(BankAccount.show_bank_name())
print(BankAccount.add_money(10))
print(BankAccount.account_size)
BankAccount.change_name('access','23')
print(lammycoal.balance)
print(lammycoal.bank_name)

class ATM:
    limit = 10000

    def __init__(self, name):
        self.name = name

    @classmethod
    def daily(cls, new_limit):
        if new_limit <= 0:
            print ("new limit cannot be zero or negative")
            return
        cls.new_limit = ATM.limit
        print(f"Today's limit is {cls.new_limit}")

    @staticmethod
    def is_valid_amount(amount):
        if not isinstance(amount, int):
            return False
        if amount <= 0:
            return False
        return True


ATM.daily(100)
print(ATM.is_valid_amount(106))

#ENCAPSULATION

class Baccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def check_balance(self):
        print(self.__balance)
        return

coal = Baccount(1000)
coal.deposit(100)
coal.__balance = 9000
# this coal.__balance doesnt change the balance instead creates a new variable
coal.withdraw(50)
coal.check_balance()

#Polymorphism(Email & Sms Notification)

class Email:
    def send(self):
        print("Email notification sent")

class Sms:
    def send(self):
        print("Sms notification sent")

notification = [Email(), Sms()]

for messages in notification:
    messages.send()

