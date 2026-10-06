class Solution:
    def climbStairs(self, n: int) -> int:
        two,one = 0, 1
        for _ in range(n):
            two,one = one, one+two
        return one