# BankAccount class banao
# Attributes: owner (naam), _balance (starting 0). Methods: deposit(amount),
#  withdraw(amount) — balance negative na ho, __str__ — nicely print ho.


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
    def withdrwa(self,amount):
        if self.balance - amount < 0:
            return f"Low balance, your current balance is {self.balance}"
        self.balance -= amount
        return f"You have withdrwan {amount} rupees and your current balance is {self.balance} "
    def __str__(self):
        return f"name:{self.owner}, balance: {self.balance}"
    

acc = BankAccount("Alex",450)
print('before deposite',acc)
acc.deposit(100)
print('after deposite',acc)
acc.withdrwa(50)
print('after withdraw',acc)




