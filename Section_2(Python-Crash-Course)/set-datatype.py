# Python Set Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Set Datatype
# URL: https://www.programiz.com/python-programming

# Set Definition: Sets are used to store multiple items in a single variable. It has the following characteristics:
# Set items are unordered, unchangeable, and do not allow duplicate values.

# (1) Create a Set in Python
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

# (2) Create an Empty Set in Python
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

# (3) Duplicate Items in a Set
# Let's see what will happen if we try to include duplicate items in a set.
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}
# Here, we can see there are no duplicate items in the set as a set cannot contain duplicates.

# (4) Add and Update Set Items in Python
# Sets are mutable. However, since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
# i. Add Items to a Set in Python
# In Python, we use the add() method to add an item to a set. For example,
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)

# ii. Update Python Set
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# (5) Remove an Element from a Set
# We use the discard() method to remove the specified element from a set. For example,
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# (6) Iterate Over a Set in Python
# (7) Find Number of Set Elements
# (8) Python Set Operations
# i. Union of Two Sets
# ii. Set Intersection
# iii. Difference between Two Sets
# iv. Set Symmetric Difference
# v. Check if two sets are equal
# (9) Built-in Functions with Set
# (10) Other Python Set Methods