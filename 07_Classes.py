class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is sitting")
    
    def roll(self):
        print(self.name.title() + " is rolling")

dog = Dog('Rex', 6)
print(dog.name)
print(dog.age)

dog.sit()
dog.roll()

class BankAccount():
    def __init__(self, code, balance=0):
        self.code = code
        self.__balance = balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
    
    def deposit(self, amount):
        self.__balance += amount
    
    def getBalance(self):
        return self.__balance


account = BankAccount('123')
print(account.getBalance())
account.deposit(100)
print(account.getBalance())
account.withdraw(50)
print(account.getBalance())