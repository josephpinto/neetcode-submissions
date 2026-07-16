class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i,c in enumerate(s):
            best_odd = c
            # odd
            l = r = i
            while l>=0 and r < len(s) and s[l] == s[r]:
                best_odd = s[l:r+1]
                l -= 1
                r += 1
            # even
            res = res if len(res) > len(best_odd) else best_odd
            if i == len(s)-1 or s[i] != s[i+1]:
                continue
            best_even = s[i:i+2]
            l,r = i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                best_even = s[l:r+1]
                l -= 1
                r += 1
          
            res = res if len(res) > len(best_even) else best_even
        return res