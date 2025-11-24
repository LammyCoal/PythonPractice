import unittest
from practice import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        self.assertEqual(BankAccount().balance, 100)

    def setUp(self):
        self.account = BankAccount()
        self.account.balance = 100

    def tearDown(self):
        self.account = None

    def test_positive_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_amount(self,amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self.account.deposit(0)
