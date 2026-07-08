class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.loan_amount = 0
        self.interest_rate = 0
        self.duration = 0
        self.emi = 0
        self.balance = 0

    def apply_loan(self, amount, rate, duration):
            self.loan_amount = amount
            self.interest_rate = rate
            self.duration = duration

            # Simple Interest Formula
            total_amount = amount + (amount * rate * duration / 100)

            self.balance =  total_amount / duration
            self.emi = total_amount / duration

    def pay_emi(self,amount):
         if amount <= self.balance:
              self.balance -= amount
              print("EMI Paid Successfully")
         else:
              print("x Amount Exceeds remaining balance")
    
    #Display customer Loan Details
    def display(self):
         print("\n-------Loan Details -------")
         print("Customer ID: ", self.cid)
         print("Customer Name:", self.name)
         print("Loan amount:", self.loan_amount)
         print("Interest Rate :", self.interest_rate)
         print("Duration:", self.duration)
         print("Monthly EMI:", round(self.emi, 2))
         print("Balance:", round(self.balance, 2))
         print("------------------------------")


class LoanManagementSystem:
     def  __init__(self):
          self.customers = []

     def find_customer(self, cid):
          for customer in self.customers:
               if customer.cid == cid:
                     return customer
          return None
    
     def add_customer(self):
          cid = int(input("Enter Customer ID:"))
          name = input("Enter Customer Name:")

          customer = Customer(cid, name)
          self.customers.append(customer)
          print("Customer Added Successfully")

    # Apply for loan
     def apply_loan(self):
          cid = int(input("Enter customer ID:"))
          customer = self.find_customer(cid)

          if customer:
               amount = float(input("Enter loan amount:"))
               rate = float(input("Enter customer ID:"))
               duration = int(input("Enter Duration (Monthly): "))

               customer.apply_loan(amount, rate, duration)

               print("Loan Approved")
          else:
               print("Customer Not Found")

     def calculate_emi(self):
          cid = int(input("Enter customer ID: "))
          customer = self.find_customer(cid)

          if customer:
               print(f"Monthly EMI is: {round(customer.emi, 2)}")
          else:
               print("X Customer Not Found ")

     def pay_emi(self):
         cid = int(input("Enter Customer ID: "))
         customer = self.find_customer(cid)

         if customer:
              amount = float(input("Enter Emi amount: "))
              customer.pay_emi(amount)

         else:
              print("X Customer Not Found")

     def view_loan(self):
            cid = int(input("Enter customer ID: "))
            customer = self.find_customer(cid)

            if customer:
                 customer.display()
            else:
                 print("customer Not Found")   

        # Display All Customers
     def display_all(self):
            if not self.customers:
                 print("No Customer Records Found")
                 return
            
            for customer in self.customers:
                 customer.display()
# Main Program

system = LoanManagementSystem()

while True:
     print("\n====== Loan Management System =======")
     print("1. Add Customer")
     print("2. Apply for loan")
     print("3. Calculate EMI")
     print("4. View loan details")
     print("5. Pay EMI")
     print("6. Display All Customers")
     print("7. Exit")

     choice = int(input("Enter Choice: "))

     if choice ==1:
           system.add_customer()
     elif choice == 2:
          system.apply_loan()
     elif choice == 3:
          system.calculate_emi()
     elif choice ==4:
          system.view_loan()
     elif choice ==5:
          system.pay_emi()
     elif choice ==6:
          system.display_all()
     elif choice == 7:
          print("System Closed X")
          break 
     else:
          print("Invalid choice")