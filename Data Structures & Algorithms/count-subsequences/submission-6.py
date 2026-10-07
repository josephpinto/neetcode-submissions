class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev_row = [0]*(len(t)+1)
        prev_row[-1] = 1
        
        for i in range(len(s)-1,-1,-1):
            new_row = [0]*(len(t)+1)
            new_row[-1] = 1
            for j in range(len(t)-1,-1,-1):
                new_row[j] = prev_row[j]
                if s[i] == t[j]:
                    new_row[j] += prev_row[j+1]
            prev_row = new_row
        return prev_row[0]

