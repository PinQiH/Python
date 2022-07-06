def gcd(m, n):
    temp = m % n
    while temp != 0:
        m = n
        n = m
        temp = m % n
    return n
    
def main():
    g = gcd(12, 18)
    print('gcd(12, 18) = ', g)