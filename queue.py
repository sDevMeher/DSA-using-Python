from collections import deque
'''
q = deque()
q.append(10)
q.append(10)
q.append(10)
q.append(10)
print(q)
'''

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

dq = Queue()
dq.enqueue(10)
dq.enqueue(20)
dq.enqueue(30)
dq.enqueue(40)
print(dq.buffer)
print(dq.size())
dq.dequeue()
print(dq.buffer)
print(dq.size())
dq.dequeue()
print(dq.buffer)
print(dq.size())
dq.dequeue()
print(dq.buffer)
print(dq.size())
dq.dequeue()
print(dq.buffer)
print(dq.size())
print(dq.is_empty())
