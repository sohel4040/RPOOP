import random

class Account:
    def __init__(self, name, acctype, balance):
        self.name = name
        self.acctype = acctype
        self.accnumber = random.randint(1790000000,1799999999)
        self.balance = balance
        
    def setBalanceToZero(self):
        self.balance = 0.0
        
    def accountHolderName(self):
        print('\033[2;31;43m',self.name,'\033[0;0m')
        
    def displayBalance(self):
        print('\033[2;31;43m',self.balance,'\033[0;0m')
        
class Transaction:
    def deposit(self, account, amount):
        account.balance = account.balance + amount
        print('\033[2;31;43m Amount deposited \033[0;0m')
    
    def withdraw(self, account, amount):
        if(account.balance > 0):
            account.balance = account.balance - amount
            print('\033[2;31;43m Amount withdrawn \033[0;0m')
        else:
            print('\033[2;31;43m Low Balance! \033[0;0m')
    
    def transferMoney(self, _from, _to, amt):
        _from.balance = _from.balance - amt
        _to.balance = _to.balance + amt


def createBankAccount():
    name = input("Enter Account holder name : ")
    acctype = input("Enter Type (Saving or Current) : ")
    balance = int(input("Enter a minimum balance you want to deposit : "))
    return Account(name, acctype, balance)

acc = None
while True:
    print("1. Create bank account")
    print("2. Deposit a amount")
    print("3. Withdraw a amount")
    print("4. Display a balance")
    print("5. Display name")
    print("6. Display account number and type")
    print("7. Exit")
    n = int(input("Enter your choice: "))
    if(n == 1):
       acc =  createBankAccount()
       print('\033[2;31;43m Account created \033[0;0m')
    elif(n == 2):
        if(acc is None):
            print('\033[2;31;43m Create the bank account first \033[0;0m')
        else:
            amt = int(input("Enter amount: "))
            t = Transaction()
            t.deposit(acc, amt)
    elif(n == 3):
        if(acc is None):
            print('\033[2;31;43m Create the bank account first \033[0;0m')
        else:
            amt = int(input("Enter amount: "))
            t = Transaction()
            t.withdraw(acc, amt)
    elif(n == 4):
        if(acc is None):
            print('\033[2;31;43m Create the bank account first \033[0;0m')
        else:
            acc.displayBalance()
    elif(n == 5):
        if(acc is None):
            print('\033[2;31;43m Create the bank account first \033[0;0m')
        else:
            print('\033[2;31;43m Account Name ',acc.name, ' \033[0;0m')
    elif(n == 6):
        if(acc is None):
            print('\033[2;31;43m Create the bank account first \033[0;0m')
        else:
            print('\033[2;31;43m Account number ',acc.accnumber, ' \033[0;0m')
            print('\033[2;31;43m Account Type ',acc.acctype, ' \033[0;0m')
    else:
        break

# t.transferMoney(person1, person2, 488)