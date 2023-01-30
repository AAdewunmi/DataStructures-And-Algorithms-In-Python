# Linear Search
# ========================
# Definition: Linear search is a sequence searching algorithm where we start
# from one end and check every element of the list until the desired element
# is found. It is the simplest searching algorithm.
#
# Linear Search Complexities
# Time Complexity: 0(n)
# Space Complexity: 0(1)
#
# Linear Search Algorithm Pseudocode
#
# LinearSearch(array, key)
# for each item in the array
#   if item == value
#      return its value
#
# Implementation
# Linear Search in Python
def linear_search(a, key):
    index = 0
    while index < len(a):
        if a[index] == key:
            return index
        index += 1
    return -1


A = [84, 21, 47, 96, 15]
found = linear_search(A, 96)
print('Result: ', found)

