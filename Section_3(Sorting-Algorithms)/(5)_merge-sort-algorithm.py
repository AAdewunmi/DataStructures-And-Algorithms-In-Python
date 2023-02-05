# Merge Sort
# ========================
# Definition: Merge Sort is a sorting algorithm that works by dividing an array into smaller sub-arrays,
# sorting each subarray, and then merging the sorted sub-arrays back together to form the final sorted array.
# In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half,
# and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
#
#
# Selection Merge Complexities
# Time Complexity:
# O(n log (n))
#
# Merge Sort Algorithm Pseudocode
# Algorithm mergesort(A, left, right)
#    if left < right then
#        mid = (left + right) / 2
#        mergesort(A, left, mid)
#        mergesort(A, mid + 1, right)
#        merge(A, left, mid, right)
#
# Algorithm merge(A, left, mid, right)
#   i = left, j = mid + 1, k = left
#   while i <= midd and j <= right
#         if A[i] < A[j] then
#             B[k] = A[i]
#             i = i + 1, k = k + 1
#          else
#             B[k] = A[j]
#             j = j + 1, k = k + 1
#    while i <= mid
#        B[k] = A[i]
#        i = i + 1, k = k + 1
#    while j <= right
#        B[k] = A[j]
#        j = j + 1, k = k + 1
#     for m = left, m <= right, m++
#        A[m] = B[m]
#
# Implementation
# Merge Sort in Python
def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right+1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        B[k] = A[i]
        i = i + 1
        k = k + 1

    while j <= right:
        B[k] = A[j]
        j = j + 1
        k = k + 1
    for x in range(left,right+1):
        A[x] = B[x]


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
mergesort(A,0,len(A)-1)
print('Sorted Array:',A)