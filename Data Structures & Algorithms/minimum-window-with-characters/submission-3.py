class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        counts = defaultdict(int)
        t_chars = set(t)
        res_l = 0
        res = ""
        for c in t:
            counts[c] += 1
        for r, c in enumerate(s):
            if c not in t_chars:
                continue
            counts[c] -= 1
            while self.hasAll(counts):
                if not res or (r-l+1) < res_l:
                    res = s[l:r+1]
                    res_l = r-l+1
                if s[l] in t_chars:
                    counts[s[l]] += 1
                l += 1
        return res
                

        

    def hasAll(self, counts):
        for count in counts.values():
            if count > 0:
                return False
        return True