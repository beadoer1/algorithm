class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 풀이
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return
    def dequeue(self):
        delete_head = self.head
        if self.is_empty():
            return "Queue is empty"
        elif self.head == self.tail: # dequeue에서 tail은...?
            self.head == None
            self.tail == None
        else:
            self.head = self.head.next
        return delete_head.data
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data
    def is_empty(self):
        return self.head == None

queue = Queue()         
queue.enqueue(3)        
print(queue.peek())     # 3
queue.enqueue(4)        
print(queue.peek())     # 3
queue.enqueue(5)       
print(queue.peek())     # 3
print(queue.dequeue())  # 3
print(queue.dequeue())  # 4
print(queue.dequeue())  # 5
print(queue.tail.data)  # tail data가 남아있음. dequeue에서 tail도 처리해주는게 맞지 않나...?