class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts = []
        stars = []

        for i,v in enumerate(s):
            if v == '(':
                lefts.append(i)
            elif v == '*':
                stars.append(i)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else: return False
        leftsCopy = lefts.copy()
        while stars and lefts:
            if stars[-1] > lefts[-1]:
                stars.pop()
                lefts.pop()
            else:
                return False
        return not lefts
