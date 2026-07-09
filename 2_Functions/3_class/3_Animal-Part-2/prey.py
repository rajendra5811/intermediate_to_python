class Animal: 
    def __init__(self, name):
        self.name = name              # main parent class
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):                   # parent class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):                # parent class
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    def legs(self):
        print(f"{self.name} has four legs")

    def fur(self):
        print(f"{self.name} is soft")

class Hawk(Predator):
    def wings(self):
        print(f"{self.name} has two wings")

    def claws(self):
        print(f"{self.name} has claws")

class Fish(Prey, Predator):
    def swims(self):
        print(f"{self.name} swims in water")


rabbit = Rabbit("Bunny")
hawk = Hawk("Tony")
fish = Fish("nemo")

rabbit.flee()
rabbit.eat()