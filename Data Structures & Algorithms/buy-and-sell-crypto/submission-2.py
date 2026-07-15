class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        curr_min = prices[0]

        for price in prices:
            max_p = max(max_p, price-curr_min)
            curr_min = min(curr_min,price)
        return max_p
