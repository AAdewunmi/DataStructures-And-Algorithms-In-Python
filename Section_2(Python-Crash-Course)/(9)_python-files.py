# Python Files
# ========================
# Adapted From: Programiz
# Tutorial Title: Python Files
# URL: https://www.programiz.com/python-programming

# A file is a container in computer storage devices used for storing data.
# When we want to read from or write to a file, we need to open it first.
# When we are done, it needs to be closed so that the resources that are tied with the file are freed.
# Hence, in Python, a file operation takes place in the following order:
#     Open a file
#     Read or write (perform operation)
#     Close the file

# (1) Opening Files in Python
# The standard way to open data from a Python file is by using the open() function.
file1 = open("test.txt")
# By default, the files are open in read mode (cannot be modified). The code above is equivalent to
file1 = open("test.txt", "r")
# Here, we have explicitly specified the mode by passing the "r" argument which means file is opened for reading.
#
# Different Modes to Open a File in Python
# Mode
# 					Description
# r
# 					Open a file for reading. (default)
# w
# 					Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x
# 					Open a file for exclusive creation. If the file already exists, the operation fails.
# a
# 					Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t
# 					Open in text mode. (default)
# b
# 					Open in binary mode.
# +
# 					Open a file for updating (reading and writing)
#
# Here's few simple examples of how to open a file in different modes,
# file1 = open("text.txt")      # equivalent to 'r' or 'rt'
# file1 = open("text.txt",'w')  # write in text mode
# file1 = open("img.bmp",'r+b') # read and write in binary mode

# (2) Reading Files in Python
#  After we open a file, we use the read() method to read its contents. For example,
# open a file
# file1 = open("test.txt", "r")
# read the file
# read_content = file1.read()
# print(read_content)

# (3) Closing Files in Python
# Closing a file will free up the resources that were tied with the file.
# It is done using the close() method in Python. For example,
# open a file
file1 = open("test.txt", "r")
# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()

# (4) Exception Handling in Files
# (5) Use of with...open Syntax
# (6) Writing to Files in Python
# (7) Python File Methods