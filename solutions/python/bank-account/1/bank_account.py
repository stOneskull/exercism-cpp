from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = None
        self.lock = Lock()

    def get_balance(self):
        if self.balance is None:
            raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.balance is not None:
            raise ValueError('account already open')
        self.balance = 0

    def deposit(self, amount):
        if self.balance is None:
            raise ValueError('account not open')
        if amount < 0:
            raise ValueError('cannot deposit negative')
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance is None:
            raise ValueError('account not open')
        if amount > self.balance:
            raise ValueError('not enough funds')
        if amount < 0:
            raise ValueError('cannot withdraw negative')
        with self.lock:
            self.balance -= amount

    def close(self):
        if self.balance is None:
            raise ValueError('account not open')
        self.balance = None
