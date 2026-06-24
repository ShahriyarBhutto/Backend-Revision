# BankAccount class banao
# Attributes: owner (naam), _balance (starting 0). Methods: deposit(amount),
#  withdraw(amount) — balance negative na ho, __str__ — nicely print ho.


# SavingsAccount extend karo BankAccount se
# Extra attribute: interest_rate (e.g. 0.05 = 5%). Extra method: add_interest() 
# jo balance pe interest add kare.

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    def deposit(self,amount):
        self.balance += amount
        return f"{amount} is added in your account , your current balance is {self.balance}"
    def withdraw(self,amount):
        if self.balance - amount < 0:
            return f"Low balance, your current balance is {self.balance}"
        self.balance -= amount
        return f"You have withdrwan {amount} rupees and your current balance is {self.balance} "
    def __str__(self):
        return f"name:{self.owner}, balance: {self.balance}"
    

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += (self.interest_rate * self.balance)/100



savacc = SavingsAccount('Hales',450)
savacc.add_interest(5)
print('savacc before deposite',savacc)
savacc.deposit(100)
print('savacc after deposite',savacc)
savacc.withdraw(50)
print('savacc after withdraw',savacc)
        
    

acc = BankAccount("Alex",450)
print('before deposite',acc)
acc.deposit(100)
print('after deposite',acc)
acc.withdraw(50)
print('after withdraw',acc)

