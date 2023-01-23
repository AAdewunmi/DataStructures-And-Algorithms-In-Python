# Python Set Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Set Datatype
# URL: https://www.programiz.com/python-programming

# Set Definition: Sets are used to store multiple items in a single variable. It has the following characteristics:
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Create a Set in Python
# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
# Let's see an example,
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Create an Empty Set in Python
# Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements, we use the set() function without any argument. For example,
# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = { }
# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))


# Duplicate Items in a Set
# Add and Update Set Items in Python
# 1. Add Items to a Set in Python
# 2. Update Python Set
# Remove an Element from a Set
# Iterate Over a Set in Python
# Find Number of Set Elements
# Python Set Operations
# 1. Union of Two Sets
# 2. Set Intersection
# 3. Difference between Two Sets
# 4. Set Symmetric Difference
# 5. Check if two sets are equal
# Built-in Functions with Set
# Other Python Set Methods