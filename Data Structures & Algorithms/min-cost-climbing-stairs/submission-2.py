class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            res = cost[i] + min(dfs(i+1), dfs(i+2))
            memo[i] = res
            return res


        return min(dfs(0),dfs(1))