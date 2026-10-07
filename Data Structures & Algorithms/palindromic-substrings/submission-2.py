class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0


        for start in range(len(s)):
            # odd
            i,j = start,start
            while i>=0 and j<len(s) and s[i] == s[j]:
                res += 1
                i-=1
                j+=1


            # even
            i,j = start,start+1
            while i>=0 and j<len(s) and s[i] == s[j]:
                res += 1
                i-=1
                j+=1
        return res