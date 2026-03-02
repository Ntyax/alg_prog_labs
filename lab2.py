import unittest

def radix_sort(arr):
    if not arr: 
        return arr
    max_val, exp = max(arr), 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in arr:
            buckets[(x // exp) % 10].append(x)

        arr = [x for bucket in buckets for x in bucket]
        exp *= 10
    return arr

def max_hamsters(S, C, hamsters):
    low, high, res = 0, C, 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            costs = []
        else:
            costs = radix_sort([h[0] + h[1] * (mid - 1) for h in hamsters])
        
        if sum(costs[:mid]) <= S:
            res, low = mid, mid + 1
        else:
            high = mid - 1
    return res
