class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        def dfs(i,j,k):
            if k == len(s3): 
                return i == len(s1) and j == len(s2)

            if (i,j,k) in memo:
                return memo[(i,j,k)]
            s1Res = False
            s2Res = False
            if i < len(s1) and s1[i] == s3[k]:
                s1Res = dfs(i+1,j,k+1)
            if j < len(s2) and s2[j] == s3[k]:
                s2Res = dfs(i,j+1,k+1)
            memo[(i,j,k)] = s1Res or s2Res
            return memo[(i,j,k)]
        return dfs(0,0,0)

