class MagicShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return sum(self.items.values())

    def __str__(self):
        return f"MagicShoppingCart({self.items})"

    def __contains__(self, item):
        return item in self.items

    
    def __iadd__(self, other):
        for item, count in other.items.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count
        return self



cart = MagicShoppingCart({'apples': 3, 'bananas': 2})
second_cart = MagicShoppingCart({'apples': 3, 'oranges': 5})


cart += second_cart
print(cart)
#polymorphism
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
  