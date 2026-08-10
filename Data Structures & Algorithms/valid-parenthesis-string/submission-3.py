class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i,c in enumerate(s):
            if c == ')':
                if not stack and not stars:
                    return False
                if stack:
                    stack.pop()
                else:
                    stars.pop()
            if c == '*':
                stars.append(i)
            if c == '(':
                stack.append(i)
        while stack:
            if not stars or stars[-1] < stack[-1]:
                return False
            stars.pop()
            stack.pop()
        return True
