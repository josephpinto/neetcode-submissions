class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1) # 0,1,...amount-1,amount

        dp[0] = 0
        for amount in range(1,amount+1):
            for coin in coins:
                remaining = amount-coin
                if remaining < 0: continue
                dp[amount] = min(dp[amount],dp[remaining]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]
            
