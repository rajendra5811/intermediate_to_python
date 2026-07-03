class House:
    layout = 'square'
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
    def paint(self, color):
        self.color = color

# We can instantiate a `home` from the class object `House`
# (using our `__init__` method!) and resolve attributes.
home = House(1000)
print(home.size)  # 1000
print(home.color)  # white

# We can resolve attributes on the class object too.
print(House.layout)  # square
print(House.paint)  # <function House.paint(self, color)>
class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
        
    # The method must be indented inside the class block
    def build_expansion(self, addition):
        self.size += addition

# Now you can create a house and expand it
home = House(2000)     
home.build_expansion(500)

print(home.size)  # Output: 2500