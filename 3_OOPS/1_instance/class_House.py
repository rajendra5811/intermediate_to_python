class House:
    layout = 'square'
    def paint(self, color):
        self.color = color

# As before, we can access attributes.
print(House.layout)  # 'square'
print(House.paint)  # <function House.paint(self, color)>

# This is the new syntax! Instantiate a class object to get back an instance object.
home = House()  # `home` is now a _specific_ instance object of type `House`
print(home)  # <House at 0x....>
print(type(home) is House)  # True

class Door:
    shape = 'rectangular'
    def open(self):
        print("Opening the door!")

front_door = Door()
class Houseboat:
    layout = 'boaty'
    def paint(self, color):
        self.color = color
#attribute resolution
home.size = '1000'
print(home.size)  # 1000
print(home.__dict__)  # {'size': '1000'}

home.color = 'red'
print(home.__dict__)  # {'size': '1000', 'color': 'red'}

home.num_bathrooms = 2
home.num_bedrooms = 3
print(home.__dict__)  # {'size': '1000', 'color': 'red', 'num_bathrooms': 2, 'num_bedrooms': 3}

home.color = 'blue'
print(home.color)  # blue
print(home.num_bathrooms)  # 2
#custom initialization
class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color

home = House(1000, color='red')
print(home.size)  # 1000
print(home.color)  # red

mansion = House(25000)
print(mansion.size)  # 25000
print(mansion.color)  # white
"""getattr(x, 'y') is equivalent to x.y. It also accepts a default fallback value if the attribute isn't found.
setattr(x, 'y', z) is equivalent to x.y = z
delattr(x, 'y') is equivalent to del x.y"""
#practise
class Notebook:
    # Double underscores before and after init are required
    def __init__(self, pages, size, spacing):
        self.pages = pages
        self.size = size
        self.spacing = spacing

# This will now run perfectly without errors
journal = Notebook(80, size='letter', spacing='wide')      
print(journal.size)