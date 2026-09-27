class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        res = 0
        for r, c in enumerate(s):
            # duplicate
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            res = max(r-l+1,res)
        return res