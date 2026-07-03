class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()
        longest = 0
        i,j = 0,0
        while j<len(s):
            if s[j] not in curr_chars:
                curr_chars.add(s[j])
                longest = max(longest, j-i+1)
                j += 1
                
            else:
                curr_chars.remove(s[i])
                i += 1
        return longest