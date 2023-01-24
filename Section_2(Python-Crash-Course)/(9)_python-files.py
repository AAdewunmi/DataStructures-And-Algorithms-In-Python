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
# file1 = open("test.txt", "r")
# read the file
# read_content = file1.read()
# print(read_content)
# close the file
# file1.close()

# (4) Exception Handling in Files
# If an exception occurs when we are performing some operation with the file,
# the code exits without closing the file. A safer way is to use a try...finally block.
# Let's see an example,
# try:
#     file1 = open("test.txt", "r")
#     read_content = file1.read()
#     print(read_content)
# finally:
#     # close the file
#     file1.close()

# (5) Use of with...open Syntax
# In Python, we can use the with...open syntax to automatically close the file. For example,
# try:
#     with open("test.txt", "r") as file1:
#         read_content = file1.read()
#         print(read_content)
# finally:
#     print("File has been read!")

# (6) Writing to Files in Python
# - Write to an existing file
try:
    with open("test.txt", "a") as file1:
        write_strings = file1.write("1_More text added to file\n"
                                    "2_More text added to file\n"
                                    "3_More text added to file")
finally:
    print("Text added to file!")
# - Read from existing file
try:
    with open("test.txt", "r") as file1:
        read_content = file1.read()
        print(read_content)
finally:
    print("Text read!")

# - Create file, then write to it
# Suppose, we don't have a file named test2.txt. Let's see what happens if we write contents to the test2.txt file.
with open("test2.txt", "w") as file2:
    # write contents to the test2.txt file
    file2.write('Programming is Fun.')
    file2.write('Programiz for beginners and enthusiasts of programming!')

# (7) Python File Methods
# Method
# 					Description
#
# close()
# 					Closes an opened file. It has no effect if the file is already closed.
#
# detach()
# 					Separates the underlying binary buffer from the TextIOBase and returns it.
#
# fileno()
# 					Returns an integer number (file descriptor) of the file.
#
# flush()
# 					Flushes the write buffer of the file stream.
#
# isatty()
# 					Returns True if the file stream is interactive.
#
# read(n)
# 					Reads at most n characters from the file. Reads till end of file if it is negative or None.
#
# readable()
# 					Returns True if the file stream can be read from.
#
# readline(n=-1)
# 					Reads and returns one line from the file. Reads in at most n bytes if specified.
#
# readlines(n=-1)
# 					Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
#
# seek(offset,from=SEEK_SET)
# 					Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()
# 					Returns True if the file stream supports random access.
#
# tell()
# 					Returns an integer that represents the current position of the file's object.
#
# truncate(size=None)
# 					Resizes the file stream to size bytes. If size is not specified, resizes to current location.
#
# writable()
# 					Returns True if the file stream can be written to.
#
# write(s)
# 					Writes the string s to the file and returns the number of characters written.
#
# writelines(lines)
# 					Writes a list of lines to the file.