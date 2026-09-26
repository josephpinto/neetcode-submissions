class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append((self.min,val))
        self.min = min(self.min,val)

    def pop(self) -> None:
        prev_min, _ = self.stack.pop()
        self.min = prev_min
        

    def top(self) -> int:
        return self.stack[-1][1]
        

    def getMin(self) -> int:

        return self.min if self.min != float('inf') else -1
        
