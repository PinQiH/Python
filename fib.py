def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    ch = ''
    n = 0
    while True:
        try:    
            n = int(input('number:'))
        except ValueError:
            print('try again')
        if n < 0:
            print('n must be > 0')
        else:
            print('fib(%d) = %d' % (n, fib(n)))
        ch = input('continue?(y/n)')
        if ch == 'n':
            break

main()
