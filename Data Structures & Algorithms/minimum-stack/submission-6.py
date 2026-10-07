class MinStack:

    def __init__(self):
        self.curr_min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val,self.curr_min))
        self.curr_min = min(self.curr_min,val)

    def pop(self) -> None:
        _, prev_min = self.stack.pop()
        self.curr_min = prev_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.curr_min
        
