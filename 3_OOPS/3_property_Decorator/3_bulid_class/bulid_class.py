class Customer:
    def __init__(self, first_name, surname, tier=('free', 0)):
        self.first_name = first_name
        self.surname = surname
        self._tier = tier[0]
        self._cost = tier[1]

    def bill_for(self, months):
        return months * self._cost

    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier

    @property
    def name(self):
        return f"{self.first_name} {self.surname}"

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, tier=('premium', 10))

# 1. Properly create a premium customer using your factory method
customer = Customer.premium("Alex", "Morgan")

# 2. Print their full name (using your @property)
print(f"Customer Name: {customer.name}")

# 3. Calculate a bill for 5 months
months_to_bill = 5
total_bill = customer.bill_for(months_to_bill)
print(f"Bill for {months_to_bill} months: ${total_bill}")