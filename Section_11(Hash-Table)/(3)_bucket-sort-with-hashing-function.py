# Bucket Sort with Hashing Function
# =================================
def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            A[position] = A[position - 1]
            position = position - 1
        A[position] = cvalue


def bucketsort(A):
    n = len(A)
    maxelement = max(A)
    l = []
    buckets = [l] * 10
    for i in range(n):
        j = int(n * A[i] / (maxelement + 1))
        if len(buckets[j]) == 0:
            buckets[j] = [A[i]]
        else:
            buckets[j].append(A[i])
    for i in range(10):
        insertionsort(buckets[i])
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            A[k] = buckets[i].pop(0)
            k = k + 1

A = [63, 250, 835, 947, 651, 28]
print('Original Array: ', A)
bucketsort(A)
print('Sort Array: ', A)