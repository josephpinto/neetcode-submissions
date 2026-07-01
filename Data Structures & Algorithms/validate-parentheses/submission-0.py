class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        joeMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            # closed paren
            if(c in joeMap.keys()):
                if len(stack) == 0:
                    return False
                if joeMap[c] != stack[-1]:
                    return False
                stack.pop()
                continue
            # opening paren
            stack.append(c)
        return len(stack) == 0
            