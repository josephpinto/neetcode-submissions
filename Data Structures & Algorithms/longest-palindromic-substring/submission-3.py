class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for start in range(len(s)):
            # odd
            i,j = start,start
            while i>=0 and j<len(s) and s[i] == s[j]:
                if (j-i+1) > len(res):
                    res = s[i:j+1]    
                i-=1
                j+=1


            ## even
            i,j = start,start+1
            while i>=0 and j<len(s) and s[i] == s[j]:
                if (j-i+1) > len(res):
                    res = s[i:j+1]    
                i-=1
                j+=1
        return res