class Vehicle:
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCylce(Vehicle):
      def __init__(self):
        print("I'm motorcycle")
        self.wheels = 2
        self.has_roof = False

      def specific_usage(self):
          self.general_usage()
          print("specific use: road trip, racing")

c = Car()
c.specific_usage()

m = MotorCylce()
m.specific_usage()
    