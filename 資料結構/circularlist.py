import sys

class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

ptr = None
current = None
prev = None

head = Student()
head.next = head

def insert():
    global head
    global ptr
    global current
    global prev
    ptr = Student()
    ptr.name = input('student name:')
    ptr.score = eval(input('student score:'))
    prev = head
    current = head.next
    #不同之處
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr

def delete():
    global head
    global prev
    global current
    del_name = ''
    #不同之處
    if head.next == head:
        print('no record')
    else:
        del_name = input('student name:')
        prev = head
        #不同之處
        while current != head and del_name != current.name:
            prev = curernt
            current = current.next
        if current != head:
            prev.next = current.next
            current = None
            print('%s record deleted' % del_name)
        else:
            print('not found')

def modify():
    global head
    global current
    global prev
    #不同之處
    if head.next == head:
        print('no record')
    else:
        modify_name = input('student name:')
        prev = head
        current = head.next
        while current != head and current.name != modify_name:
            prev = current
            current = current.next
        if current != head:
            print('student name: %s' % current.name)
            print('student score: %d' % current.score)
            prev.next = current.next
            current = None
            newscore = eval(input('student new score:'))
            ptr = Student()
            ptr.name = modify_name
            ptr.score = newscore
            ptr.next = None
            prev = head
            current = head.next
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
        else:
            print('not found')

def display():
    global head
    global current
    count = 0

    if head.next == head:
        print('no record')
    else:
        current = head.next
        while current != head:
            print(current.name, current.score)
            count += 1
            current = current.next
        print('total %d record' % count)

def main():
    option = True
    while True:
        print('1.insert')
        print('2.delete')
        print('3.modify')
        print('4.display')
        print('5.exit')
        try:
            option = eval(input('choice:'))
        except ValueError:
            print('not a correct number')
            print('try again')
        if option == 1:
            insert()
        elif option == 2:
            delete()
        elif option == 3:
            modify()
        elif option == 4:
            display()
        else:
            sys.exit(0)

main()

