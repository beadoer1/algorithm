import sys

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        return
    
    def push(self,value):
        tmp = self.head
        self.head = Node(value)
        self.head.next = tmp
        return 

    def pop(self):
        if self.empty() == 1:
            return -1
        tmp = self.head
        self.head = self.head.next
        return tmp.data

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def empty(self):
        if self.head != None:
            return 0
        return 1

    def top(self):
        if self.empty() == 1:
            return -1
        return self.head.data

num_instruct = int(sys.stdin.readline())
stack = Stack()

for i in range(num_instruct):
    instruction = list(sys.stdin.readline().split())
    if instruction[0] == 'push':
        stack.push(instruction[1])
    elif instruction[0] == 'pop':
        print(stack.pop())
    elif instruction[0] == 'size':
        print(stack.size()) 
    elif instruction[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())

