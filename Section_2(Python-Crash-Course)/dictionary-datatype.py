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

# (6) Python Dictionary Methods
# (7) Dictionary Membership Test
# (8) Iterating Through a Dictionary