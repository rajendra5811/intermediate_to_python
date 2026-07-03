class House:
    appliances = []
    def __init__(self, size):
        self.size = size
    def install(self, appliance):
        self.appliances.append(appliance)
home = House(1000)
vacation_home = House(5000)

home.install('oven')
home.install('microwave')
print(home.appliances)  # ['oven', 'microwave'] - good! what we wanted
print(vacation_home.appliances)  # ['oven', 'microwave'] - oh no! we didn't want this

print(id(home.appliances))  # => 45...1632
print(home.__dict__)  # {'size': 1000}
print(House.__dict__)
# {
#     'appliances': ['oven', 'microwave']
#     ... other stuff
# }

print(House.appliances)  # ['oven', 'microwave']
print(id(House.appliances))  # 45...1632
print(id(vacation_home.appliances))  # 45...1632

#Instance vs. Class Attribute Resolution
class Vehicle:
    def __init__(self, color="white"):
        self.color = color  # Now it's an instance attribute right from the start

    def repaint(self, color):
        self.color = color

# 1. Create the vehicle with a custom color
v = Vehicle(color='red')

# 2. Check the object's internal dictionary
print(v.__dict__)