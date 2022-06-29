#單向鏈結的加入、刪除

import sys

class Student:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.score = 0
        self.next = None

prev = None
current = None
ptr = None

head = Student()
head.id = 0
head.name = ''
head.score = 0
head.next = None

tail = None

#新增
def insert():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.next = None
    ptr.id = eval(input('\n 請輸入id:'))
    ptr.name = input('\n 請輸入name:')
    ptr.score = eval(input('\n 請輸入score:'))
    print()

    prev = head
    current = head.next
    while current != None:
        prev = current 
        current = current.next
    ptr.next = tail
    prev.next = ptr

#刪除
def delete():
    global head
    global current

    if head.next == None:
        print('\n 無資料')
    else:
        current = head.next
        head.next = current.next
        current = None    
        print('已刪除')        
        print()

#輸出
def display():
    global head
    global current
    
    count = 0

    if head.next == head:
        print('\n無資料')
    else:
        print('\n%-10s %-15s %-10s' % ('ID', 'NAME', 'SCORE'))
        current = head.next
        while current != None:
            print('%-3d %-15s %-3d' % (current.id, current.name, current.score))
            count += 1
            current = current.next
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

