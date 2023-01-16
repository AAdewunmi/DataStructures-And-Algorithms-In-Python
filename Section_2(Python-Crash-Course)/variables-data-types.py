# Variables and Data Types
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Variables, Constants and Literals
# URL: https://www.programiz.com/python-programming/variables-constants-literals

# Python Variables, Constants, Literals and print()
# Definition: Variables are used to store values
# =================================================
# =================================================


# (1) Assigning values to Variables in Python
# Assign (=) value "10" to numbers variable
numbers = 10
# Print Output
print(10)

# (2) Changing the Value of a Variable in Python
site_name = 'python-data-structures-and-algorithms.com'
# Print Output
print(site_name)
# assigning a new value to site_name
site_name = 'python-is-the-best.com'
# Print Output
print(site_name)

# (3) Assigning multiple values to multiple variables
a, b, c = 99, 675.25, 'Ere, dere, an, everywhere!'
print(a)  # prints 99
print(b)  # prints 675.25
print(c)  # prints Ere, dere, an, everywhere!
# (3.i) Assigning the same value to multiple variables
website1 = website2  = 'learn-python-app.com'
print(website1)  # prints learn-python-app.com
print(website2)  # prints learn-python-app.com

# (4) Rules for Naming Python Variables
# Constants and variables should have a combination of letters in lowercase (a to z),
# or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:
# snake_case, MACRO_CASE, camelCase, CapWords.
#
# Avoid using keywords like if, True, class, etc. as variable names.
# For more information, see "PEP 8 – Style Guide for Python Code"
# https://peps.python.org/pep-0008/

# (5) Python Constants
# A constant is a special type of variable whose value cannot be changed.
# In Python, constants are usually declared and assigned in a module (a new file containing variables, functions, etc. which is imported to the main file).
# Declare Constants
PI = 3.14
Eulers_Number = 2.71828
#
print(PI) # prints 3.14
print(Eulers_Number) # prints 2.71828
#
#Note: In reality, we don't use constants in Python. Naming them in all capital letters is a convention to separate them from variables, however, it does not actually prevent reassignment.

# (6) Python Literals
# Literals are representations of fixed values in a program. They could be numbers, characters, or strings etc. For example, 'Python is cool', 24, 99.73, 'Z'
# site_name is a variable, and 'programming.python' is a literal.
site_name = 'programming.python'
print(site_name)

# (7) Python Numeric Literals
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float and Imaginary Numbers
# Some examples of integer literals:
print(7, 2147483647, 0o177, 0b100110111)
print(3, 79228162514264337593543950336, 0o377, 0xdeadbeef)
print(100_000_000_000, 0b_1110_0101)

# (8) Python Boolean Literals
# There are two boolean literals: True and False
# For example:
boolean_literal = True
# Print
print(boolean_literal)
# Here True is a boolean literal assigned to boolean_literal


# (9) String and Character Literals in Python
# Character literals are unicode characters enclosed in a quote. For example:
a_character = 'A'
# Print
print(a_character)
# Here, A is a character literal assigned to a_character.
# Similarly, String literals are sequences of Characters enclosed in quotation marks.
# For example:
a_string = 'Python is fun'
# Print
print(a_string)
# Here, 'Python is fun' is a string literal assigned to a_string.

# (10) Special Literal in Python
# Python contains one special literal None. We use it to specify a null variable. For example,
value = None
print(value)
# Output: None
# Here, we get None as an output as the value variable has no value assigned to it.

# (11) Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
# list literal
fruits = ["apple", "mango", "orange"]
print(fruits)

# tuple literal
numbers = (1, 2, 3)
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'}
print(vowels)

# In the above example, we created a list of fruits, a tuple of numbers, a dictionary of alphabets having values with keys designated to each value and a set of vowels.

# Python Data Types
# =================
# =================
# In computer programming, data types specify the type of data that can be stored inside a variable.

# (1) Python Numeric Data type
# In Python, numeric data type is used to hold numeric values.
# Integers, floating-point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.
#
# int - holds signed integers of non-limited length.
# float - holds floating decimal points and it's accurate up to 15 decimal places.
# complex - holds complex numbers.
#
# We can use the type() function to know which class a variable or a value belongs to.
#
# Let's see an example,
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

# In the above example, we have created three variables named num1, num2 and num3 with values 5, 5.0, and 1+2j respectively.
#
# We have also used the type() function to know which class a certain variable belongs to.
#
# Since,
#
#     5 is an integer value, type() returns int as the class of num1 i.e <class 'int'>
#     2.0 is a floating value, type() returns float as the class of num2 i.e <class 'float'>
#     1 + 2j is a complex number, type() returns complex as the class of num3 i.e <class 'complex'>

# (2) Python String Data Type
# String is a sequence of characters represented by either single or double quotes. For example,
name_of_language = 'Python'
print(name_of_language)
message_to_all = 'Learn Python in 24 hours, as if!'
# In the above example, we have created string-type variables: name_of_language and message_to_all with values 'Python' and 'Learn Python in 24 hours, as if!' respectively.

# (3) Python List Data Type
# List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]. For example,
programming_languages = ["Java", "Python", "JavaScript"]
print(programming_languages)
# Here, we have created a list named programming_languages with 3 string values inside it.

# (4) Python Tuple Data Type
# Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
# In Python, we use the parentheses () to store items of a tuple. For example,
product = ('Xbox', 499.99)
print(product)
# Here, product is a tuple with a string value Xbox and integer value 499.99.

# (5) Python Set Data Type
# Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }. For example,
# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))

# Here, we have created a set named student_info with 5 integer values.
# Since sets are unordered collections, indexing has no meaning. Hence, the slicing operator [] does not work.

# (6) Python Dictionary Data Type
# Python dictionary is an unordered collection of items. It stores elements in key/value pairs.
# Here, keys are unique identifiers that are associated with each value.
# Let's see an example,
# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)

# In the above example, we have created a dictionary named capitalCity. Here,
#     1. Keys are 'Nepal', 'Italy', 'England'
#     2. Values are 'Kathmandu', 'Rome', 'London'
# When we run this code, we might get output in a different order. This is because the dictionary has no particular order.