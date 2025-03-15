

# Basic Method
class Student:
    def greet(self):
        print("Welcome to college")


s = Student()
s.greet()


# Method with parameters
class Student:
    def greet(self, name):
        print(f"Hello, {name}")

s = Student()
s.greet("Hemanth")


#  Constructor Method
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


    def details(self):
        print(f"Student: {self.name}, roll no: {self.roll_no}")

s = Student("Hemanth", 25)
s.details()

# Class Method
class Student:
    college_name = 'SJB Institute of Science and Technology'

    @classmethod
    def college_details(cls):
        print(f"College name: {cls.college_name}")

Student.college_details()

# Static Method
class MathUtils:

    @staticmethod
    def add(a,b):
        return a + b

result = MathUtils.add(2,3)

print(result)