class Solution:
    def climbStairs(self, n: int) -> int:
        oneBack, twoBack = 2,1
        if n == 2:
            return 2
        if n == 1:
            return 1
        for _ in range(3,n+1):
            newVal = oneBack+twoBack
            twoBack = oneBack
            oneBack = newVal
        return oneBack

        