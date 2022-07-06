def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def main():
    ch = ''
    n = 0
    while True:
        try:
            n = int(input('number:'))
        except ValueError:
            print('try again')
        print('%d! = %d' %(n, fact(n)))
        ch = input('continue?(y/n)')
        if ch == 'n':
            break

main()