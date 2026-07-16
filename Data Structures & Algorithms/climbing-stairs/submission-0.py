class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0]*(n+1)
        if n == 1:
            return 1
        results[0] = 1
        results[1] = 1

        for i in range(2,n+1):
            print(results)
            results[i] = results[i-1] + results[i-2]
        return results[-1]