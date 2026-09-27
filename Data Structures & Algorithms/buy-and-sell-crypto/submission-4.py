class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]
        for p in prices[1:]:
            if p > curr_min:
                profit = max(profit, p-curr_min)
            else:
                curr_min = p



        return profit