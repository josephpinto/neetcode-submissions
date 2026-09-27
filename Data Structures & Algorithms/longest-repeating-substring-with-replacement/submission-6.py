class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0]*26
        maxx = 0
        l = 0
        for r,c in enumerate(s):
            chars[ord(c)-ord('A')] += 1
            max_char_count = max(chars)
            while sum(chars)-k-max_char_count > 0:
                chars[ord(s[l])-ord('A')] -= 1
                l += 1
            maxx = max(maxx, (r-l+1))
        return maxx