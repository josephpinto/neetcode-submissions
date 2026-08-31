class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buying or selling state
        memo = {}
        def dfs(i,isBuying):
            if i >= len(prices):
                return 0
            if (i,isBuying) in memo:
                return memo[(i,isBuying)]
            # if buying, can buy or skip
            res = 0
            if isBuying:
                res =  max(dfs(i+1,False)-prices[i], dfs(i+1,True))
            # sell now or skip
            else:
                res = max(prices[i]+dfs(i+2,True), dfs(i+1,False))
            memo[(i,isBuying)] = res
            return res
        return dfs(0,True)
