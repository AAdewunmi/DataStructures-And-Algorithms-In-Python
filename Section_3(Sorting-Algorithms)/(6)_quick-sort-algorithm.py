# Quick Sort
# ========================
# Definition: Quicksort is a sorting algorithm based on the divide and conquer approach where
# An array is divided into sub-arrays by selecting a pivot element (element selected from the array).
# While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
# The left and right sub-arrays are also divided using the same approach. This process continues until each subarray contains a single element.
# At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
#
# Quick Sort Complexities
# Time Complexity: O(n2)
#
# Quick Sort Algorithm Pseudocode
# Algorithm quicksort(A, low, high)
#    if low < high then
#       pi = partition(A, low, high)
#       quicksort(A, low, pi - 1)
#       quicksort(A, pi + 1, high)
#
#  Algorithm partition(A, low, high):
#    pivot = A[low]
#    i = low, j = high
#    do
#       do
#          i = i + 1
#        while(A[i] <= pivot)
#        do
#          j = j - 1
#        while(A[j] > pivot)
#        if i < j then
#            swap(A[i], A[j])
#     while(i < j)
#     swap(A[low], A[j])
#     return j
#
# Implementation
# Quick Sort in Python
def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


A = [3, 5, 8, 9, 6, 2, 1]
print('Original Array: ', A)
quicksort(A, 0, len(A) - 1)
print('Sorted Array: ', A)
