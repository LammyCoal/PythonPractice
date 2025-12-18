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
        self.balance = 0
        BankAccount.change_size()

    def balance(self):
        print(f'Bank ID: {self.name}, Balance: {self.balance}')

    @classmethod
    def change_name(cls, new_name):
        cls.bank_name = new_name

    @classmethod
    def change_size(cls):
        cls.account_size += 5

lammycoal = BankAccount('Lammy', 22)
edu = BankAccount('Edu', 23)
print(BankAccount.account_size)
print(BankAccount.change_name('access'))
print(lammycoal.balance)
print(lammycoal.bank_name)
