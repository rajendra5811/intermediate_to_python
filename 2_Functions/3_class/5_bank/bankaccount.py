class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        if amount >0:
            self._balance += amount
            print(f"Deposited Rs. {amount} to your account! New balance: Rs {self._balance}")
        else:
            print("Invalid amount, Please try again!")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"withdrawn amount Rs. {amount}, New balance: Rs {self._balance}")
        else:
            print("Insufficient fund!")
    
    def show_balance(self):
        print(f"Hi {self.name}, your balance is: Rs {self._balance}")

    
account1 = BankAccount("Alex", 1000)
account1.deposit(2000)
account1.withdraw(500)
account1.show_balance()