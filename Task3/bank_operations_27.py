# 27.Write a class that represents a bank account, do bank operations.

class Bank_Account:
    bank_name = 'ICICI'
    branch = 'channai'
    ifsc_code = 'ICICI123'

    def __init__(self,name,acc_no,acc_bal):
        self.name = name
        self.Acc_no = acc_no
        self.Acc_bal = acc_bal

person1 = Bank_Account('moin',1000,1234)
print(person1)


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.deposit(amount)
            print(f"Transfer of {amount} successful. Current balance: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")
per = BankAccount(123,'moin',5000)
per.deposit(400)
per.transfer(400,124)
