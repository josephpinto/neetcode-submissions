class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0]*(len(text2)+1)

        for i in range(len(text1)-1,-1,-1):
            curr = [0]*(len(text2)+1)
            for j in range(len(text2)-1,-1,-1):
                # skip letter in either string
                curr[j] = max(prev[j], curr[j+1])
                # have a match
                if text1[i] == text2[j]:
                    curr[j] = max(curr[j], 1 + prev[j+1])
            prev = curr
        return prev[0]