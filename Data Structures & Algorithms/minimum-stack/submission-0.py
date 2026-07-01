class StoredValue:
    def __init__(self, value, prevMin):
        self.value = value
        self.prevMin = prevMin

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
    def push(self, val: int) -> None:
        
        self.stack.append(StoredValue(val, self.min))
        self.min = min(self.min, val)

    def pop(self) -> None:
        storedValue = self.stack.pop()
        if storedValue.value == self.min:
            self.min = storedValue.prevMin

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.min
        
