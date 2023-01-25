# Python Class and Object
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Class and Object
# URL: https://www.programiz.com/python-programming

# Python is a versatile programming language that supports various programming styles,
# including object-oriented programming (OOP) through the use of classes and objects.

# (1) Python Classes
# We use the class keyword to create a class in Python. For example,
class Bike:
    name = ""
    gear = 0

# (2) Python Objects
# An object is called an instance of a class. For example, suppose Bike is a class then we can create objects like bike1, bike2, etc. from the class.
# Here's the syntax to create an object.
# create class
class Bike:
    name = ""
    gear = 0
# create objects of class
bike1 = Bike()
bike2 = Bike()

# (3) Access Class Attributes Using Objects
# We use the . notation to access the attributes of a class. For example,
# define a class
class Bike:
    name = ""
    gear = 0
# create object of class
bike1 = Bike()
# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"
print(f"Name: {bike1.name}, Gears: {bike1.gear}")

# (4) Create Multiple Objects of Python Class
# define a class
class Employee:
    # define an attribute
    employee_id = 0
# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()
# access attributes using employee1
employee1.employee_id = 1001
print(f"Employee ID: {employee1.employee_id}")
# access attributes using employee1
employee1.employee_id = 1002
print(f"Employee ID: {employee1.employee_id}")

# (5) Python Methods
# We can also define a function inside a Python class.
# A Python Function defined inside a class is called a method.
# Let's see an example,
# create a class
class Room:
    length = 0.0
    breadth = 0.0
    # method to calculate area
    def calculate_area(self):
        print("Area of Room = ", self.length * self.breadth)
# create object of Room class
study_room = Room()
# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8
# access method inside class
study_room.calculate_area()

# (6) Python Constructors
#  We can also initialize values using the constructors. For example,
class Bike:
    # constructor function
    def __init__(self, name="", gear=0):
        self.name = name
        self.gear = gear
# create bicycle objects
bike1 = Bike("Mountain Bike", 11)
bike2 = Bike("City Bike", 6)
# print objects
def print_object_details(bike):
    print(f"Name: {bike.name}, Gears: {bike.gear}")
print_object_details(bike1)
print_object_details(bike2)

# (7) Python Inheritance
# (8) Python Encapsulation
# (9) Python Polymorphism