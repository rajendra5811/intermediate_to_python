class Student:
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display(self):
        print(f"{self.roll_no}\t{self.name}\t{self.course}\t{self.marks}")

class StudentManagementSystem:
    def  __init__(self):
        self.students = []

    def add_student(self):
        roll_no = int(input("Enter Student Roll No:  "))
        name = input("Enter STUDENT Name: ")
        course = input("Enter Course: ")
        marks =  float(input("Enter Marks:  "))

        student = Student(roll_no, name, course, marks)
        self.students.append(student)
        print("V Student Added successfully")

    def display_students(self):
        if not self.students:
            print("No Student Record Found!")
            return
        print("\n Roll No\t name \t course \t marks")
        print("-------------------------------------")
        for student in self.students:
             student.display()

    def search_student(self):
        roll_no = int(input("Enter roll No To search students: "))
        for student in self.students:
            if student.roll_no == roll_no:
                print("V Student Found.")
                student.display()
                return
        print("X student Not Found!")
   
    def update_student(self):
        roll_no = int(input("Enter roll No to update student:  "))
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter New Name:")
                student.course = input("Enter New Course:")
                student.marks = float(input("Enter New Marks:"))
                print("v Student Updated Successfully!")
                return
        print("X Student Not Found!")

    def delete_student(self):
        roll_no = int(input("Enter roll No To delete students: "))
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("V Student deleted Successfully")
                return
        print("X student Not Found!")

sms = StudentManagementSystem()

while True:
    print("\n=====Student Management System =======")
    print("1. Add Student. ")
    print("2. Display Students ")
    print("3. Search Student. ")
    print("4. Update Student. ")
    print("5. Delete Student.")
    print("6. Exit. ")

    choice = int(input("Enter Your choice: "))

    if choice == 1:
        sms.add_student()
    elif choice == 2:
        sms.display_students()
    elif choice == 3:
        sms.search_student()
    elif choice == 4:
        sms.update_student()
    elif choice == 5:
        sms.delete_student()
    elif choice == 6:
        print("Thank You , Student")
        break
    else:
        print("Invalid Choice!")
                      
