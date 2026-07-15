class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_length = 0 
        for r, char in enumerate(s):
            while char in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(char)
            max_length = max(max_length,r-l+1)

        return max_length
