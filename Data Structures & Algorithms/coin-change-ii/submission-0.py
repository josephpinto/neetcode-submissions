class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount   0 , 1,2,... amount
        # coins  1
        #        2
        #        5
        # eliminate duplicates by considering the row as "use coins up to and including this row"
        ROWS,COLS = len(coins)+1, amount+1
        dp = [[0]*(COLS) for _ in range(ROWS)]
        # 1 way to make 0
        for row in range(ROWS):
            dp[row][0] = 1
        for row in range(ROWS-2,-1,-1):
            for amt in range(1,COLS):
                dp[row][amt] += dp[row+1][amt]
                coin = coins[row]
                if amt-coin < 0:
                    continue
                dp[row][amt] += dp[row][amt-coin]

        return dp[0][amount]