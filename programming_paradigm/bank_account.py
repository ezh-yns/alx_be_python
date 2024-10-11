class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if (amount > 0):
            self.account_balance += amount
            print(f"Deposited: $ {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if (amount > 0 and amount <= self.account_balance):
            self.account_balance -= amount
            print(f"Withdrew: $ {amount}")
        else:   
            print("Withdrawal amount must be positive and not exceed the account balance.")

    def display_balance(self):
        print(f"Current Balance: $ {self.account_balance}")


# bankAccount = BankAccount()
# result = bankAccount.deposit(5000.0)
# result = bankAccount.withdraw(1500.0)
# result = bankAccount.display_balance()
