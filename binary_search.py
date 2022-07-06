def binary_search(a, x, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, x, left, mid - 1)
    else:
        return binary_search(a, x, mid + 1, right)
        
import random
a = sorted([8, 19, 36, 43, 50, 52, 55, 65, 71, 81])
print(binary_search(a, 65, 0, len(a) - 1))