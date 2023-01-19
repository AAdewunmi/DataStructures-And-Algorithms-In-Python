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

# Python for loop with else

# 4. Python while Loop
# ----------------------
# 5. Python break and continue
# -----------------------------
# 6. Python Pass
# ---------------