class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None]*(len(s)+1)
        def dfs(i):
            if memo[i] != None:
                return memo[i]
            if i == len(s):
                return True
            if i > len(s):
                return False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                     if dfs(i+len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
                