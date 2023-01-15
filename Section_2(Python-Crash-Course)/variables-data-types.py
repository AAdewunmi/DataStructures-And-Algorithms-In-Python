# Variables and Data Types
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Variables, Constants and Literals
# URL: https://www.programiz.com/python-programming/variables-constants-literals

# Python Variables, Constants, Literals and print()
# Definition: Variables are used to store values

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
# (11) Literal Collections