class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_counts = [float('inf')]*(amount+1) # 0,1 ... amount
        coin_counts[0] = 0
        for curr_amount in range(1, amount+1):
            for coin in coins:
                remaining = curr_amount - coin
                if remaining < 0:
                    continue
                # min of this coin and other coins
                coin_counts[curr_amount] = min(coin_counts[curr_amount], 1 + coin_counts[remaining])
        
        return coin_counts[-1] if coin_counts[-1] != float('inf') else -1