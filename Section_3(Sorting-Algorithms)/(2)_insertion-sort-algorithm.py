# Insertion Sort Algorithm
# ========================
# Definition:
# Insertion sort is a sorting algorithm places an unsorted element at its
# suitable place in each iteration. The algorithm assumes that the first
# element is already sorted then, selects an unsorted element. If the unsorted element
# is greater than the first element, it is placed on the right otherwise,
# to the left. In the same way, other unsorted elements are taken and put
# in their place.
#
# Insertion Sort Complexity
# O(n2)
#
# Insertion Sort Algorithm
# Algorithm insertion-sort(A)
#   n = length(A)
#   for i = 1, i < n, i++
#       cvalue = A[i]
#       position = i
#       while position > 0 and A[position] > cvalue
#           A[position] = A[position - 1]
#           position = position - 1
#        A[position] = cvalue
#
# Insertion Sort Algorithm Implementation
def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            A[position] = A[position - 1]
            position = position - 1
        A[position] = cvalue


A = [3, 5, 8, 9, 6, 2]
print(A)
insertionsort(A)
print(A)