def quicksort(a, low, high):
    if high > low:
        pivotpoint = partition(a, low, high)
        quicksort(a, low, pivotpoint - 1)
        quicksort(a, pivotpoint + 1, high)
        
def partition(a, low, high):
    pivotitem = a[low]
    j = low
    for i in range(low + 1, high + 1):
        if a[i] < pivotitem:
            j += 1
            a[i], a[j] = a[j], a[i]
    pivotpoint = j
    a[low], a[pivotpoint] = a[pivotpoint], a[low]
    return pivotpoint

import random
a = random.sample(range(100), 10)
print(a)
a = quicksort(a, 0, len(a) - 1)
print(a)