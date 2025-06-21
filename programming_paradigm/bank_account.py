# this script that simulates simple bank account transactions from the command line

class BankAccount:

    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    # deposit amount adds the specified amount to account_balance
    def deposit(self, amount):
        #self.initial_balance += amount
        self.account_balance += amount

    # withdraw deduct the amount from account balance if funds are sufficient
    # returning True; otherwise, return False and does not alter the balance
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    # display balance prints the current balance in the account
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
