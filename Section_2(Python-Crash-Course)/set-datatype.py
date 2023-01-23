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
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
    print(fruit)

# (7) Find Number of Set Elements
# We can use the len() method to find the number of elements present in a Set. For example,
even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))

# (8) Python Set Operations
# Python Set provides different built-in methods to perform mathematical set operations like union, intersection, subtraction, and symmetric difference.

# i. Union of Two Sets
# We use the | operator or the union() method to perform the set union operation. For example,
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))

# ii. Set Intersection
# In Python, we use the & operator or the intersection() method to perform the set intersection operation. For example,
# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# iii. Difference between Two Sets
# We use the - operator or the difference() method to perform the difference between two sets. For example,
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# iv. Set Symmetric Difference
# In Python, we use the ^ operator or the symmetric_difference() method to perform symmetric difference between two sets. For example,
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('using ^:', A ^ B)
# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))



# (9) Built-in Functions with Set
# (10) Other Python Set Methods