# Shell Sort Algorithm
# ========================
# Definition:
# Shell sort is a generalised version of the insertion sort algorithm.
# It first sorts elements that are far apart from each other and successively
# reduces the interval between the elements to be sorted.
#
# Shell Sort Complexity
# Θ(N(log N))
#
# Shell Sort Algorithm
# Algorithm shell-sort(A)
#   n = length(A)
#   for gap = n/2, gap>0, gap = gap/2
#       for i=gap, i<n, i++
#           gvalue = A[i]
#           j = i - gap
#           while j >= 0 and A[j] > gvalue
#                A[j + gap] = A[j]
#                j = j - gap
#            A[j + gap] = gvalue
#
# Shell Sort Algorithm Implementation
def shellsort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            i = i + 1
        gap = gap // 2


A=[3, 5, 8, 9, 6, 2]
print(A)
shellsort(A)
print(A)