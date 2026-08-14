class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append((val, self.curr_min))
        self.curr_min = min(self.curr_min, val)

    def pop(self) -> None:
        popped_val, prev_min = self.stack.pop()
        if popped_val == self.curr_min:
            self.curr_min = prev_min


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.curr_min
