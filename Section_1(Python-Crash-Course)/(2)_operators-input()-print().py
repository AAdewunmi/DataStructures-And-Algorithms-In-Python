# Python Operators, input() and print()
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Operators, input() and print()
# URL: https://www.programiz.com/python-programming

# Python Basic Input and Output (I/0)
# 1. Python print()
# Definition: In Python, we can simply use the print() function to print output.
# Syntax: print()

# Example 1: Python Print Statement
print('Good Morning!')
print('It is rainy today')

# Example 2: Python print() with end Parameter
# print with end whitespace
print('Good Morning!', end= ' ')
print('It is rainy today')

# Example 3: Python print() with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')

# Output formatting
# Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method. For example,
x = 17
y = 1
z = 2023
print('The value of x is {}, y is {} and z is {}'.format(x,y,z))

# 2. Python input()
# Definition: In Python, we use the input() function to take input from the user.
# Syntax: input(prompt)
# using input() to take user input

num = input('What is your date of birth? : ')
print('You Entered:', num)
print('Data type of num:', type(num))

# In the above example, we have used the input() function to take input from the user and stored the user input in the num variable.
# It is important to note that the entered value at the prompt is a string, not a number. So, type(num) returns <class 'str'>.
# To convert user input into a number we can use int() or float() functions as:

num = int(input('What is your date of birth?'))
print('You Entered:', num)
print('Data type of num:', type(num))

# =====================
# =====================
# Python Operators
# Operators are special symbols that perform operations on variables and values.
# Types of Python Operators
# 1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. For example,

a = 7
b = 2

# addition
print ('Sum: ', a + b)

# subtraction
print ('Subtraction: ', a - b)

# multiplication
print ('Multiplication: ', a * b)

# division
print ('Division: ', a / b)

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)

# a to the power b
print ('Power: ', a ** b)

# 2. Assignment Operators
# Assignment operators are used to assign values to variables.

# Assignment Operator: a = 10

# Addition Assignment: '+=' // a += 1 # a = a + 1

# Subtraction Assignment: '-=' // a -= 3 # a = a - 3

# Multiplication Assignment: '*=' // a *= 4 # a = a * 4

# Division Assignment: '/=' // a /= 3 # a = a / 3

# Remainder Assignment: '%=' // a %= 10 # a = a % 10

# Exponent Assignment: a **= 10 # a = a ** 10

# 3. Comparison Operators
# Definition: Comparison operators compare two values/variables and return a boolean result: True or False. For example,

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

# 4. Logical Operators
# Definition: Logical operators are used to check whether an expression is True or False. They are used in decision-making. There are three operators 'and', 'or', 'not'
# For example,
a = 5
b = 6
print((a > 2) and (b >= 6))    # True
# Here, and is the logical operator AND. Since both a > 2 and b >= 6 are True, the result is True.

# Logical AND (a and b):
# True only if both the operands are True

# Logical OR (a or b):
# True if at least one of the operands is True

# Logical NOT (not a):
# True if the operand is False and vice-versa.

# 5. Bitwise Operators
# Definition: Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
# For example, 2 is 10 in binary and 7 is 111.

# In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

# Operator:     Meaning:      Example:

# &           Bitwise AND      x & y = 0 (0000 0000)
# |            Bitwise OR      x | y = 14 (0000 1110)
# ~           Bitwise NOT      ~x = -11 (1111 0101)
# ^           Bitwise XOR      x ^ y = 14 (0000 1110)
# >>      Bitwise right shift  x >> 2 = 2 (0000 0010)
# <<      Bitwise left shift   x << 2 = 40 (0010 1000)

# 6. Special Operators
# Definition: Python language offers some special types of operators like the identity operator and the membership operator. They are described below with examples.

# 1. Identity operators
# Definition: In Python, 'is' and 'is not' are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

# Operator:     Meaning:                            Example:
# is     True if the operands are identical        x is True
#           (refer to the same object)
# is not True if the operands are not identical    x is not True
#        (do not refer to the same object)

# Example: Identity operators in Python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# Here, we see that x1 and y1 are integers of the same values, so they are equal as well as identical. Same is the case with x2 and y2 (strings).
# But x3 and y3 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.

# 2. Membership operators
# Definition: In Python, in and not in are the membership operators. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

# In a dictionary we can only test for presence of key, not the value.

#  Operator:          Meaning:                                  Example:
# in True    if value/variable is found in the sequence          5 in x
# not in   True if value/variable is not found in the sequence  5 not in x

# Example: Membership operators in Python

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False

# Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive).
 # Similarly, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.