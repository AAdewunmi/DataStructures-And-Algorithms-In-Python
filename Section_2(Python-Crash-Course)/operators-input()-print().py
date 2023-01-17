# Python Operators, input() and print()
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Variables, Constants and Literals
# URL: https://www.programiz.com/python-programming/variables-constants-literals

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
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Special Operators
