class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for c in s:
            if c not in paren_map:
                stack.append(c)
            else:
                if not stack or stack[-1] != paren_map[c]:
                    return False
                stack.pop()
        return not stack