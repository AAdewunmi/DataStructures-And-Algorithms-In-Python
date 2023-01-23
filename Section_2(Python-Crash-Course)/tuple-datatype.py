# Python Tuple Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python List Datatype
# URL: https://www.programiz.com/python-programming

# Tuple Definition: Tuples are used to store multiple items in a single variable. It has the following characteristics:
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# (1) Create a Tuple
# A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.
# A tuple can have any number of items, and they may be of different types (integer, float, list, string, etc.).
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# (2) Create a Python Tuple With one Element
# In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.
# We will need a trailing comma to indicate that it is a tuple,
var1 = ("Hello") # string
var2 = ("Hello",) # tuple

# (3) Access Python Tuple Elements
# 1. Indexing
# 2. Negative Indexing
# 3. Slicing
# (4) Python Tuple Methods
# (5) Iterating through a Tuple in Python
# (6) Check if an Item Exists in the Python Tuple
# (7) Advantages of Tuple over List in Python