def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    u = merge_sort(a[:m])
    v = merge_sort(a[m:])
    return merge(u, v)

def merge(u, v):
    a = []
    i = j = 0
    while i < len(u) and j < len(v):
        if u[i] <= v[j]:
            a.append(u[i])
            i += 1
        else:
            a.append(v[j])
            j += 1
    return a + u[i:] + v[j:]
    
import random
a = random.sample(range(100), 10)
print(a)
a = merge_sort(a)
print(a)