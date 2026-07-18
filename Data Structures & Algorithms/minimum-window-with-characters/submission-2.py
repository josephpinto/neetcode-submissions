class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        res = ""
        res_len = 0
        t_chars = set()
        for char in t:
            t_chars.add(char)
            counts[char] = counts.get(char,0)+1
        l = 0

        for r, char in enumerate(s):
            if char not in t_chars:
                continue
            counts[char] -= 1
            while self.allCovered(counts):
                if not res or r-l+1 < res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                if s[l] in t_chars:
                    counts[s[l]] += 1
                l += 1
        return res
            

    def allCovered(self, counts):
        for c in counts.values():
            if c > 0:
                return False
        return True
