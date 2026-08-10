class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, target):
            if target == 0:
                return 1
            if target < 0 or i == len(coins):
                return 0
            if (i,target) in memo:
                return memo[(i,target)]
            res = 0
            
            coin = coins[i]
            res += dfs(i,target-coin)
            # decide to stop using coin
            res += dfs(i+1, target)
            memo[(i,target)] = res
            return res
        return dfs(0, amount)