# Bucket Sort with Hashing Function
# =================================
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