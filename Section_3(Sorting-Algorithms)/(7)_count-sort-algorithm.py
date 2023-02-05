# Count Sort
# ========================
# Definition: Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array.
# The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
#
# Count Sort Complexities
# Time Complexity: O(n)
#
# Count Sort Algorithm Pseudocode
# Algorithm count-sort(A)
#     n = length(A)
#     maxsize = max(A)
#     carray = [0, 0, .... maxsize + 1]
#     for i = 0, i < n, i++
#         carray[A[i]] = carray[A[i]] + 1
#     i, j = 0
#     while i < maxsize + 1
#         if carray[i] > 0 then
#            A[j++] = i
#            carray[i] = carray[i] - 1
#          else
#             i = i + 1
#
# Implementation
# Count Sort in Python

def countsort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize + 1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1


A = [3, 5, 8, 9, 6, 2, 1]
print('Original Array: ', A)
countsort(A)
print('Sorted Array: ', A)
