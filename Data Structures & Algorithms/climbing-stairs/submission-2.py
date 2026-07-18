class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        stairs = [0]*(n+1)
        stairs[0] = stairs[1] = 1
        for step in range(2,n+1):
            stairs[step] = stairs[step-1] + stairs[step-2]
        return stairs[n]