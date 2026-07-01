class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorSet = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token in operatorSet:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.compute(token,a,b))
            else:
                stack.append(int(token))
        return stack.pop()

    def compute(self,token,a,b):
        if(token == '+'):
            return b+a
        if token == '-':
            return b-a
        if token == '/':
            return int(b/a)
        if token == '*':
            return b*a
