class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(width , height)

    def Area(self, width, height):
          print("the area is:", width * height)

    def circumference(self, width, height):
         print("the circumference of rectangle:", 4*width*height)

rect = Rectangle(5,6)
rect.Area(5,6)
rect.circumference(5,6)
print(rect.width, rect.height)
          