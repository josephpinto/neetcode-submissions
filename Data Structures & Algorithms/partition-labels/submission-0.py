class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        farthest = [0]*26
        for i,char in enumerate(s):
            farthest[ord(char)-ord('a')] = i
        
        res = []
        l = 0
        chars = set()
        for r, char in enumerate(s):
            chars.add(char)
            all_covered = True
            for curr_char in chars:
                if farthest[ord(curr_char)-ord('a')] > r:
                    all_covered = False
            if all_covered:
                res.append(r-l+1)
                l = r+1
                chars = set()
        return res


