class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        stairs = [0]*(n+1)
        first,second = 1,1
        for step in range(2,n+1):
            new_step = first+second
            first,second = second,new_step
        return second