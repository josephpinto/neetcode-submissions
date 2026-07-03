class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        max_length = 1
        most_common_char = s[0]
        l = r = 0
        
        while r<len(s):
            char = s[r]
            counts[ord(char)-ord('A')] += 1

            while r-l+1 - max(counts) > k:
                counts[ord(s[l])-ord('A')] -= 1
                l += 1

            max_length = max(max_length, r-l+1)
            r += 1  

        return max_length
