from datetime import datetime


# -------------------- 1. Customer --------------------
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display_customer(self):
        print("\nCustomer Information")
        print("---------------------")
        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)


# -------------------- 2. Account --------------------
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.balance


# -------------------- 3. Transaction --------------------
class Transaction:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, action, amount):
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.transactions.append((date, action, amount))

    def show_transactions(self):
        print("\nTransaction History")
        print("------------------------")
        if len(self.transactions) == 0:
            print("No Transactions")
        else:
            for t in self.transactions:
                print(t)


# -------------------- 4. Login --------------------
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, user, pwd):
        return self.username == user and self.password == pwd


# -------------------- 5. Receipt --------------------
class Receipt:
    def print_receipt(self, customer, account):
        print("\n=========== RECEIPT ===========")
        print("Customer :", customer.name)
        print("Account  :", account.account_no)
        print("Balance  : ₹", account.get_balance())
        print("===============================")


# -------------------- 6. ATM --------------------
class ATM:
    def deposit_cash(self, account, transaction):
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)
        transaction.add_transaction("Deposit", amount)

    def withdraw_cash(self, account, transaction):
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)
        transaction.add_transaction("Withdraw", amount)


# -------------------- 7. Bank --------------------
class Bank:
    def __init__(self, name):
        self.name = name

    def display_bank(self):
        print("\nWelcome to", self.name)


# -------------------- 8. Menu --------------------
class Menu:
    def display(self):
        print("\n========= BANK MENU =========")
        print("1. Customer Details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Print Receipt")
        print("7. Exit")


# -------------------- 9. BankSystem --------------------
class BankSystem:
    def __init__(self):
        self.bank = Bank("ABC Bank")

        self.customer = Customer(101, "Rajendra")
        self.account = Account(123456789, 10000)

        self.transaction = Transaction()
        self.login = Login("admin", "1234")
        self.receipt = Receipt()
        self.atm = ATM()
        self.menu = Menu()

    def start(self):
        self.bank.display_bank()

        username = input("Username: ")
        password = input("Password: ")

        if not self.login.authenticate(username, password):
            print("Invalid Login")
            return

        while True:
            self.menu.display()

            choice = input("Enter Choice: ")

            if choice == "1":
                self.customer.display_customer()

            elif choice == "2":
                self.atm.deposit_cash(self.account, self.transaction)

            elif choice == "3":
                self.atm.withdraw_cash(self.account, self.transaction)

            elif choice == "4":
                print("Current Balance: ₹", self.account.get_balance())

            elif choice == "5":
                self.transaction.show_transactions()

            elif choice == "6":
                self.receipt.print_receipt(self.customer, self.account)

            elif choice == "7":
                print("Thank You for Using ABC Bank")
                break

            else:
                print("Invalid Choice")


# -------------------- 10. Main --------------------
class Main:
    def run(self):
        bank = BankSystem()
        bank.start()


# Driver Code
if __name__ == "__main__":
    app = Main()
    app.run()