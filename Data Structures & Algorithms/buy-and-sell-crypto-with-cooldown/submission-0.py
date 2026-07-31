class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in cache: return cache[(i,buying)]

            if buying:
                # buy or cooldown
                cache[(i,buying)] = max(-prices[i]+dfs(i+1, False), dfs(i+1,True))
            else:
                cache[(i,buying)] =  max(prices[i]+dfs(i+2, True), dfs(i+1,False))
            return cache[(i,buying)]
        return dfs(0,True)