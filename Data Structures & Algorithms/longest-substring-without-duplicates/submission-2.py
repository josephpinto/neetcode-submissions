class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        res = 0
        for r, c in enumerate(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            res = max(res, r-l+1)
        return res
            