class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(animal):
      def speak(self):
           print("braking")

class Cat(animal):
        def speak(self):
           print(" meow!")
           
class Mouse(animal):
        def speak(self):
            print("SQUEEK!")
            
cat = Cat("doramon")
mouse = Mouse("Mickey")
mouse.eat()
mouse.sleep()
mouse.speak()
cat.eat()
cat.speak()


    