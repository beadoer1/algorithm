# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 풀이 1: 런타임 에러..;;
# import sys

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         return

#     def push(self, value):
#         new_node = Node(value)
#         if self.empty() == 1:
#             self.head = new_node
#             self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node
#         return

#     def pop(self):
#         if self.empty() == 1:
#             return -1
#         tmp_head = self.head
#         if self.head == self.tail:
#             self.tail = None
#         self.head = self.head.next
#         return tmp_head.data

#     def size(self):
#         count = 0
#         cur_node = self.head
#         while cur_node is not None:
#             cur_node = cur_node.next
#             count += 1
#         return count

#     def empty(self):
#         if self.head == None:
#             return 1
#         return 0
    
#     def front(self):
#         if self.empty == 1:
#             return -1
#         return self.head.data
    
#     def back(self):
#         if self.empty == 1:
#             return -1
#         return self.tail.data

# num_instruct = int(sys.stdin.readline())
# queue = Queue()
# for i in range(num_instruct):
#     instruction = list(sys.stdin.readline().split())
#     if instruction[0] == 'push':
#         queue.push(instruction[1])
#     elif instruction[0] == 'pop':
#         print(queue.pop())
#     elif instruction[0] == 'size':
#         print(queue.size())
#     elif instruction[0] == 'empty':
#         print(queue.empty())
#     elif instruction[0] == 'front':
#         print(queue.front())
#     else:
#         print(queue.back())

# 풀이 2: 그냥 list가지고 하자 _ ...시간 초과 -_-;;;
# import sys
# num_instruct = int(sys.stdin.readline())
# queue = []
# for i in range(num_instruct):
#     instruction = list(sys.stdin.readline().split())
#     if instruction[0] == 'push':
#         queue.append(instruction[1])
#     elif instruction[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue.pop(0))
#     elif instruction[0] == 'size':
#         if not queue:
#             print(-1)
#         else:
#             print(len(queue))
#     elif instruction[0] == 'empty':
#         if queue:
#             print(0)
#         else:
#             print(1)
#     elif instruction[0] == 'front':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#     else:
#         if not queue:
#             print(-1)
#         else:
#             print(queue[len(queue)-1])

# 풀이 3: deque 이용하자.. 와 '맞았..ㅠ'
import sys
import collections

num_instruct = int(sys.stdin.readline())
queue = collections.deque()

for i in range(num_instruct):
    instruction = list(sys.stdin.readline().split())
    if instruction[0] == 'push':
        queue.append(instruction[1])
    elif instruction[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif instruction[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])