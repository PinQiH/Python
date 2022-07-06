#1
'''
a = set(list(range(1, 100, 2)))
b = set(list(range(0, 101, 5)))
aandb = a & b
print('交集', aandb)
print()
bothab = a | b
print('聯集', bothab)
print()
onlya = a - b
print('ab差集', onlya)
print()
onlyb = b - a
print('ba差集', onlyb)
print()
noab = a ^ b
print('ab對稱差集', noab)
print()
noba = b ^ a
print('ba對稱差集', noba)
print()
'''

#2
'''
a = set(list(range(1, 100, 2)))
b = []
def isprime(n):
    if n == 2:
        b.append(n)
    elif n > 2:
        for i in range(2, n): 
            if n % i == 0:
                break
            else:
                b.append(n)
                break
for j in range(1, 101):
    isprime(j)
b = set(b)
aandb = a & b
print('交集', aandb)
print()
bothab = a | b
print('聯集', bothab)
print()
onlya = a - b
print('ab差集', onlya)
print()
onlyb = b - a
print('ba差集', onlyb)
print()
noab = a ^ b
print('ab對稱差集', noab)
print()
noba = b ^ a
print('ba對稱差集', noba)
print()
'''
