class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# 강의 답변 : 앞쪽으로 쌓인다는 관점
class Stack:
    def __init__(self):
        self.head = None
    def push(self,value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head
    def peek(self):
        # if self.is_empty():
        #     return "Stack is empty"
        return self.head.data
    def is_empty(self):
        if self.head == None:
            return True
        return False

stack = Stack()
stack.push(2)
stack.push(5)
print(stack.peek())
print(stack.pop().data)
print(stack.is_empty())
print(stack.peek())
stack.pop()
print(stack.is_empty())