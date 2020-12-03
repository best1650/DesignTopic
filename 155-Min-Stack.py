class MinStack():

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, x):
        self.stack.append(x)
        minNum = x
        
        if len(self.minStack) > 0:
            minNum = min(x,self.minStack[-1])
            
        self.minStack.append(minNum)

    def pop(self):
        if len(self.stack) > 1:
            self.stack.pop()
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin()) # return -3
ms.pop()
print(ms.top())    # return 0
print(ms.getMin()) # return -2
        
