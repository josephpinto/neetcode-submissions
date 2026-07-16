from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        required_counts = defaultdict(int)
        l = 0
        res = ""
        for char in t:
            required_counts[char] -= 1


        for r, char in enumerate(s):
            print('r, char',r, char)
            if char in required_counts:
                required_counts[char] += 1
            while self.allNonNegative(required_counts):
                if res == "":
                    res = s[l:r+1]
                elif len(res) > r-l+1:
                    res = s[l:r+1]
                if s[l] in required_counts:
                    print('removing required char')
                    required_counts[s[l]] -= 1
                l += 1
                print('shrinking the loop')
            print('required_counts', required_counts)
        return res

    def allNonNegative(self,counts):
        for count in counts.values():
            if count < 0:
                return False
        return True