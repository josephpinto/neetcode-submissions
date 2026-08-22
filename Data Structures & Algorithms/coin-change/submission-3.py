class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for target in range(1,amount+1):
            for c in coins:
                remaining = target-c
                if remaining >= 0:
                    dp[target] = min(dp[target],1+dp[remaining])
        return dp[-1] if dp[-1] != float('inf') else -1


            
        