# Python Flow Control
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Flow Control
# URL: https://www.programiz.com/python-programming

# 1. Python if ... else
# ----------------------
# In Python, there are three forms of the 'if ... else' statement:
# i. if statement
# Example 1: Python if Statement
number = 10
# check if number is greater than 0
if number > 0:
    print('Number is positive.')
print('The if statement is easy')

# ii. if ... else statement
# Example 2. Python if...else Statement
number = 10
# check if number is greater than 0
if number > 0:
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')

# iii.if ... elif ... else statement
# Example 3: Python if...elif...else Statement
number = 0
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')
print('This statement is always executed')

# 2. Python Nested if statements
# -------------------------------
# Example 4: Python Nested if Statement
number = 5
# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
# outer else statement
else:
    print('Number is negative')
# Output: Number is positive


# 3. Python for Loop
# -------------------
# Definition: In Python, the for loop is used to run a block of code for a certain number of times.
# It is used to iterate over any sequences such as lists, tuples, string, etc.
# Example: Loop Over Python List
programming_languages = ['Swift', 'Python', 'Go', 'JavaScript']
for language in programming_languages:
    print(language)

# Python for Loop with Python range()
# A 'range' is a series of values between two numeric intervals.
# We use Python's built-in function range() to define a range of values. For example,
# use of range() to define a range of values
values = range(4)
# iterate from i = 0 to i = 3
for i in values:
    print(i)

# Python for loop with else
# Definition: A 'for' loop can have an optional else block as well. The 'else' part is executed when the loop is finished. For example,
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")


# 4. Python while Loop
# ----------------------
# Definition: Python while loop is used to run a specified code until a certain condition is met.
# Example 1: Python while Loop
i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

# Example 2: Python while Loop to Display Game Level
current_level = 0
final_level = 5
game_completed = True
while current_level <= final_level:
    if game_completed:
        print('You have passed level', current_level)
        current_level += 1
print('Level Ends')

# Infinite while Loop in Python
# Python While loop with else
# Python for vs while loops

# 5. Python break and continue
# -----------------------------
# 6. Python Pass
# ---------------