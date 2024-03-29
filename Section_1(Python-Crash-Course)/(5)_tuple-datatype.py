# Python Tuple Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Tuple Datatype
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
# We can use the index operator [] to access an item in a tuple, where the index starts from 0.
# accessing tuple elements using indexing
# 1. Indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])   # prints "p"
print(letters[5])   # prints "a"

# 2. Negative Indexing
# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on. For example,
# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[-1])   # prints 'z'
print(letters[-3])   # prints 'm'

# 3. Slicing
# We can access a range of items in a tuple by using the slicing operator colon :.
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')
# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')
# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# (4) Python Tuple Methods
# In Python ,methods that add items or remove items are not available with tuple. Only the following two methods are available.
# Some examples of Python tuple methods:
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

# (5) Iterating through a Tuple in Python
# We can use the for loop to iterate over the elements of a tuple. For example,
languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for language in languages:
    print(language)

# (6) Check if an Item Exists in the Python Tuple
# We use the in keyword to check if an item exists in the tuple or not. For example,
languages = ('Python', 'Swift', 'C++')
print('C' in languages)    # False
print('Python' in languages)    # True

# (7) Advantages of Tuple over List in Python
# Since tuples are quite similar to lists, both of them are used in similar situations.
# However, there are certain advantages of implementing a tuple over a list:
#
#     We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
#     Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
#     Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
#     If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.