#雙向鏈結串列的加入、刪除

import sys

class Student:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.score = 0
        self.llink = None
        self.rlink = None

prev = None
current = None
ptr = None

head = Student()
head.name = ''
head.llink = head
head.rlink = head

#新增
def insert():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.id = eval(input('\n 請輸入id:'))
    ptr.name = input('\n 請輸入name:')
    ptr.score = eval(input('\n 請輸入score:'))
    print()

    prev = head
    current = head.rlink
    while current != head:
        prev = current 
        current = current.rlink
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink = ptr

#刪除
def delete():
    global head
    global current
    global prev

    if head.rlink == head:
        print('\n 無資料')
    else:
        prev = head
        current = head.rlink
        
        if head != current:
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            print('已刪除')
        else:
            print('無法刪除資料')
        
        print()

#輸出
def display():
    global head
    global current
    
    count = 0

    if head.rlink == head:
        print('\n無資料')
    else:
        print('\n%-10s %-15s %-10s' % ('ID', 'NAME', 'SCORE'))
        current = head.rlink
        while current != head:
            print('%-3d %-15s %-3d' % (current.id, current.name, current.score))
            count += 1
            current = current.rlink
        print('共 %d 筆資料\n' % count)

def main():
    option = 0

    while True:
        print('1.insert')
        print('2.delete')
        print('3.display')
        print('4.exit')

        try:
            option = int(input('choice:'))
        except ValueError:
            print()
            print('Not a correct number')
            
        if option == 1:
            insert()
        elif option == 2:
            delete()
        elif option == 3:
            display()
        elif option == 4:
            sys.exit(0)

main()

