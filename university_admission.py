# Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
# Age is greater than 20
# Marks is between 0 and 100 (both inclusive)
# A student qualifies for admission, if
# Age and marks are valid and
# Marks is 65 or more
# Write a python program to represent the students seeking admission in the university. The details of student class are given below


class Student:
    def __init__(self,student_id, marks,age):
        self.__student_id=student_id
        self.__marks=marks
        self.__age=age
    
    def get_studentID(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    
    def set_studentID(self,id):
        self.__student_id=id
    def set_marks(self,updated_marks):
        self.__marks=updated_marks
    def set_age(self,new_age):
        self.__age=new_age
    

    def validate_marks(self):
        if 0<=self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.__marks>=65:
            return "Qualified for admission"
        else:
            return "Not Qualified"

students = [
    Student(1, 21, 70),
    Student(2, 22, 50),
    Student(3, 19, 85),
    Student(4, 23, 95),
    Student(5, 18, 75)
]

print("Students qualifying for admission:")
for student in students:
    if student.check_qualification():
        print(f"Student ID: {student.get_studentID()}, Age: {student.get_age()}, Marks: {student.get_marks()}")