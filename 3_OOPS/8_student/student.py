class student:
    rno = 123
    name = 'abc'
    branch = "cse"
    test = 'ST-100'

    def read(self):
     rno = 345
     print("rollno =",rno)
     print("Instance variable =", self.rno)
     print("reading")

    def write(self):
     print("Writing...")

     def test(self):
       subject = 'G-101'
       print("test is 2 hours with 180 questions",test)
       
       
abc = student()
obj = student()
print("rno =", student.rno)
print("name =", student.name)
print("branch =",abc.branch)
abc.read()
abc.write()