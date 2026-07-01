class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxResult = 0 
        minNum = float('inf')

        for price in prices:
            profit = price-minNum
            maxResult = max(maxResult,profit)
            minNum = min(minNum,price)

        return maxResult