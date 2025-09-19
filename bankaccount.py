class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        self.balance -=amount
    def check_balance(self):
        return self.balance
account=BankAccount()
account.deposit(200)
account.withdraw(50)
print(account.check_balance())