# Python Dictionary Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Dictionary Datatype
# URL: https://www.programiz.com/python-programming

# Dictionary Definition: Dictionaries are used to store data values in key:value pairs. It has the following characteristics:
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# (1) Create a dictionary in Python
# Example i: Python Dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)
# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# (2) Add Elements to a Python Dictionary
# We can add elements to a dictionary using the name of the dictionary with []. For example,
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)

# (3) Change Value of Dictionary
# We can also use [] to change the value associated with a particular key. For example,
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
student_id[112] = "Stan"
print("Updated Dictionary: ", student_id)

# (4) Accessing Elements from Dictionary
# In Python, we use the keys to access their corresponding values. For example,
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters

# (5) Removing elements from Dictionary
# We use the del statement to remove an element from the dictionary. For example,
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)

# (6) Dictionary Membership Test
# We can test if a key is in a dictionary or not using the keyword in. Notice that the membership test is only for the keys and not for the values.
# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares) # prints True
print(2 not in squares) # prints True
# membership tests for key only not value
print(49 in squares) # prints false

# (7) Iterating Through a Dictionary

# (8) Python Dictionary Methods
# Methods that are available with a dictionary are tabulated below. Some of them have already been used in the above examples.
# Function
# 					Description
#
# all()
# 					Return True if all keys of the dictionary are True (or if the dictionary is empty).
#
# any()
# 					Return True if any key of the dictionary is true. If the dictionary is empty, return False.
#
# len()
# 					Return the length (the number of items) in the dictionary.
#
# sorted()
# 					Return a new sorted list of keys in the dictionary.
#
# clear()
# 					Removes all items from the dictionary.
#
# keys()
# 					Returns a new object of the dictionary's keys.
#
# values()
# 					Returns a new object of the dictionary's values