class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxx = 0
        l = 0
        counts = [0]*26
        for r, c in enumerate(s):
            counts[ord(c)-ord('A')] += 1
            max_count = max(counts)
            while l < r and sum(counts)- max_count > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1
            maxx = max(maxx, r-l+1)


        return maxx