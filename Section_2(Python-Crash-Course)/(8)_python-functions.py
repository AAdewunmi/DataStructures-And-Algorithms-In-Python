# Python Functions
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Functions
# URL: https://www.programiz.com/python-programming

# A function is a block of code that performs a specific task.
# Suppose, you need to create a program to create a circle and color it. You can create two functions to solve this problem:
#     create a circle function
#     create a color function
# Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

# Types of function
# There are two types of function in Python programming:
# Standard library functions - These are built-in functions in Python that are available to use.
# User-defined functions - We can create our own functions based on our requirements.

# Python Function Declaration
# The syntax to declare a function is:
# def function_name(arguments):
    # function body
    # return
# Here,
#     def - keyword used to declare a function
#     function_name - any name given to the function
#     arguments - any value passed to function
#     return (optional) - returns value from a function
# Let's see an example,
def greet():
    print('Hello World!')

# Calling a Function in Python
# To use a function, we need to call it.
# For example,
def greet():
    print('Hello World!')
# call the function
greet()
print('Outside function')

# Python Function Arguments
# As mentioned earlier, a function can also have arguments. An argument is a value that is accepted by a function. For example,
# Example 1: Python Function (function with two arguments)
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)
# function call with two values
add_numbers(5, 4)

# Example 2: Python Function Arguments (The return Statement in Python)
# A Python function may or may not return a value. If we want our function to return some value to a function call, we use the return statement. For example,
# function definition
def find_square(num):
    result = num * num
    return result
# function call
square = find_square(5)
print('Square:',square)

# Python Library Functions
# In Python, standard library functions are the built-in functions that can be used directly in our program. For example,
#
#     print() - prints the string inside the quotation marks
#     sqrt() - returns the square root of a number
#     pow() - returns the power of a number
#
# These library functions are defined inside the module. And, to use them we must include the module inside our program.
#
# For example, sqrt() is defined inside the math module.
import math
# sqrt computes the square root
square_root = math.sqrt(4)
print("Square Root of 4 is ", square_root)
# pow() computes the power
power = pow(2, 3)
print("2 to the power 3 is ", power)

# Benefits of Using Functions