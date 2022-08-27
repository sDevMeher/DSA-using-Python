from collections import deque
#stack = deque()
#print(dir(stack)) --print all the methods and function of the deque module
'''
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack.pop())'''

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container) 
        
