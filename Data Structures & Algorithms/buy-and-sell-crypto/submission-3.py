class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        curr_min = prices[0]

        for p in prices[1:]:
            maxP = max(maxP,p-curr_min)
            curr_min = min(curr_min,p)



        return maxP