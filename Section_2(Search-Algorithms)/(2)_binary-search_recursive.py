# Binary Search (Recursive Approach)
# ========================
# Definition: Binary Search is searching algorithm for finding an element's
# position in a sorted array. In this approach, the element is always searched
# in the middle of a portion of an array.
# Binary search can be implemented only on a sorted list of items.
# If the elements are not sorted already, we need to sort them first.
#
# Binary Search Complexities
# Time Complexity: 0(log n)
# Space Complexity: 0(1)
#
# Binary Search Working
#
# Binary Search Algorithm can be implemented in two ways which are discussed below.
#
#     Iterative Method
#     Recursive Method
#
# Binary Search Algorithm Pseudocode (Recursive Approach)
#
# binarySearch(arr, x, low, high)
#       if low > high
#           return False
#       else
#           mid = (low + high) / 2
#       if x == arr[mid]
#            return mid
#       else if x > arr[mid] // x is on the right side
#            return binarySearch(arr, x, mid + 1, high)
#       else                 // x is on the left side
#            return binarySearch(arr, x, low, mid - 1)
#
# Implementation
# Binary Search in Python (Recursive Approach)
def binary_search_r(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binary_search_r(A, key, l, mid - 1)
        elif key > A[mid]:
            return binary_search_r(A, key, l, mid + 1, r)


A = [15, 21, 47, 84, 96]
found = binary_search_r(A, 47, 0, 4)
print('Result: ', found)