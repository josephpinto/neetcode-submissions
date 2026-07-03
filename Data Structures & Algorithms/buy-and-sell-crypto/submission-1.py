class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = prices[0]
        for price in prices[1:]:
            result = max(result, price-minPrice)
            minPrice = min(minPrice,price)



        return result
