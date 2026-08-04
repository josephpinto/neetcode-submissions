class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        prev = [0]*(len(t)+1)
        prev[-1] = 1

        for i in range(len(s)-1,-1,-1):
            newRow = [0]*(len(t)+1)
            newRow[-1] = 1
            for j in range(len(t)-1,-1,-1):    
                newRow[j] = prev[j]
                if s[i] == t[j]:
                    newRow[j] += prev[j+1]
            prev = newRow
            
        return prev[0]