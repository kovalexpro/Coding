import numpy as np

class ArrayStack():
    def __init__(self, n):
        self.array = np.zeros(n, dtype=int)
        self.n = n
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self, x):
        if self.top >= self.n - 1:
            print('The stack is full')
            return
        else:
            self.top += 1
            self.array[self.top] = x

    def pop(self):
        if self.isEmpty():
            print('The stack is empty')
            return
        else:
            ret = self.array[self.top]
            self.top -= 1
            return ret

    def printStack(self):
        if self.isEmpty():
            print('The stack is empty')
            return
        for i in (self.top, -1):
            print(self.array[i])

class Node():
    def __init__(self, x, node):
        self.x = x
        self.previous = node


class PointerStack():
    def __init__(self):
        self.top = Node('', -1)

    def isEmpty(self):
        if self.top.previous == -1:
            return True
        else:
            False

    def push(self, x):
        if self.isEmpty():
            node = Node(x, self.top)
            self.top= node
        else:
            node = Node(x, self.top)
            self.top = node

    def pop(self):
        if self.isEmpty():
            print('The stack is empty')
            return
        else:
            ret = self.top
            self.top = self.top.previous
            return ret

    def printStack(self):
        if self.isEmpty():
            print('The stack is empty')
            return
        while True:
            ret = self.top.x
            if ret != '':
                self.top = self.top.previous
                print(ret)
            else:
                break
            
arrStack = ArrayStack(5)
arrStack.printStack()

poiStack = PointerStack()
poiStack.printStack()