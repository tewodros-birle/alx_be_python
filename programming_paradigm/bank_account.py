
class BankAccount:
    """A simple bank account class that handles deposits, withdrawals, and balance checks"""
    
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance"""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist"""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
