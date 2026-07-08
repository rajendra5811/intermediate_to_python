class Employee:
      
      def __init__(self, name, age,salary):
            self.name = name
            self.age = age
            self.salary = salary

      def work(self):
            print(f"{self.name} is working...")     

class SoftwareEngineer(Employee):
      
    def __init__(self, name, age, salary):
          super().__init__(name, age, salary)
          self.salary = salary
    def work(self):
         print(f"{self.name} is coding..")
    def debug(self):
          print(f"{self.name} is debugging...")

class Designer(Employee):
      
    def draw(self):
         print(f"{self.name} is drawing...")
se = SoftwareEngineer(name = "Max", age = 25, salary = 60000)
se.work()
se.debug()


d = Designer("Philipp", 27, 70000)
d.work()
d.draw()