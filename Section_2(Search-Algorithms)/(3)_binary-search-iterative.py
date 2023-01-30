# Binary Search (Iterative Approach)
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
# Binary Search Algorithm Pseudocode (Iterative Approach)
#
# do until the pointers low and high meet each other.
#   mid = (low + high)/2
#   if (x == arr[mid])
#       return mid
#   else if (x > arr[mid])  // x is on the right side
#       low = mid + 1
#   else                    // x is on the left side
#       high = mid - 1
#
# Implementation
# Binary Search in Python (Iterative Approach)
def binary_search_i(a, key):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = l + r // 2
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            r = mid - 1
        elif key > a[mid]:
            l = mid + 1
    return -1


A = [15, 21, 47, 84, 96]
found = binary_search_i(A, 47)
print('Result: ', found)