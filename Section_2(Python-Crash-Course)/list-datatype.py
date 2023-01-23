# Python List Datatype
# ========================
# Adapted From: Programiz
# Tutorial Title: Python List Datatype
# URL: https://www.programiz.com/python-programming

# List Definition: A list is a collection of similar types of data. It has the following characteristics:
# List items are ordered, changable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc

# (1) Create a Python List
# A list is created in Python by placing items inside [], separated by commas . For example,
# A list with 3 integers
numbers = [1, 2, 5]
print(numbers)
# Output: [1, 2, 5]

# A list can have any number of items, and they may be of different types (integer, float, string, etc.). For example,
# empty list
my_list = []
# list with mixed data types
my_list = [1, "Hello", 3.4]

# (2) Access Python List Elements
# In Python, each item in a list is associated with a number. The number is known as a list index.
# We can access elements of an array using the index number (0, 1, 2 …). For example,

languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[0])   # Python
# access item at index 2
print(languages[2])   # C++

# (3) Negative Indexing in Python
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
# Let's see an example,

languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[-1])   # C++
# access item at index 2
print(languages[-3])   # Python


# (4) Slicing of a Python List
# In Python it is possible to access a section of items from the list using the slicing operator :, not just a single item. For example,
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']
# items from index 2 to index 4
print(my_list[2:5])
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])

# (5) Add Elements to a Python List
# Python List provides different methods to add items to a list.
# 1. Using append()
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)
# 2. Using extend()
prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)
even_numbers = [4, 6, 8]
print("List2:", even_numbers)
# join two lists
prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers)

# (6) Change List Items
# Python lists are mutable. Meaning lists are changeable. And, we can change items of a list by assigning new values using = operator. For example,
languages = ['Python', 'Swift', 'C++']
# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']

# (7) Remove an Item From a List
# 1. Using del()
# In Python we can use the del statement to remove one or more items from a list. For example,
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']
# delete first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)

# 2. Using remove()
# We can also use the remove() method to delete a list item. For example,
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# remove 'Python' from the list
languages.remove('Python')
print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# (8) Iterating through a List
# (9) Check if an Item Exists in the Python List
# (10) Python List Length
# (11) Python List Comprehension
# (12) Python List Methods