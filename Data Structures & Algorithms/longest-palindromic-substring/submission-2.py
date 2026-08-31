class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        for i in range(len(s)):
            # odd
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > len(res):
                    res = curr
                l -= 1
                r += 1
            
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > len(res):
                    res = curr
                l -= 1
                r += 1
        return res