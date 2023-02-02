# Selection Sort Algorithm
# ========================
# Definition:
# Selection sort is a sorting algorithm that selects the smallest
# element from an unsorted list in each iteration and places that
# element at the beginning of the unsorted list.
#
# Selection Sort Complexity
# O(n2)
#
# Selection Sort Algorithm
# Algorithm selection-sort(A)
#   n = length(A)
#   for i = 0, i < n - 1, i++
#       position = i
#       for j = i + 1, j < n, j++
#           if A[J] < A[position] then
#               position = j
#       temp = A[i]
#       A[i] = A[position]
#       A[position] = temp
#
# Selection Sort Algorithm Implementation
def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        position = i
        for j in range(i + 1, n):
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp


A = [3, 5, 8, 9, 6, 2]
print(A)
selectionsort(A)
print(A)

