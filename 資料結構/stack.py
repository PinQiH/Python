#堆疊的新增、刪除

import sys
MAX = 8
st = [''] * MAX
top = -1

#新增
def push():
    global MAX
    global st
    global top

    if top >= MAX - 1:
        print('\n 堆疊是滿的')
    else:
        top += 1
        st[top] = input('\n字串資料:')
    print()

#刪除
def pop():
    global st
    global top
    
    if top < 0:
        print('\n 堆疊是空的')
    else:
        print('\n %s 已被刪除！' % st[top])
        top -= 1
    print()

#輸出
def list():
    global st
    global top

    count = 0
    
    if top < 0:
        print('\n 堆疊是空的！')
    else:
        print('\n 堆疊有下列的資料：')
        print('-------------------')
        i = top
        while i >= 0:
            print(' ', end = '')
            print(st[i])
            count += 1
            i -= 1
        print('共有%d筆資料\n' % count)
    print()

def main(): 
    option = 0

    while True:
        print('1.push')
        print('2.pop')
        print('3.list')
        print('4.exit')

        try:
            option = eval(input('Choice：'))
        except ValueError:
            print()
            print('Not a correct number.')

        if option == 1:
            push()
        elif option == 2:
            pop()
        elif option == 3:
            list()
        else:
            sys.exit(0)

main()
