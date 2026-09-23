class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = self.getKey(s)
            groups[key].append(s)
        res = []
        for group in groups.values():
            res.append(list(group))
        return res
    

    def getKey(self,s):
        counts = [0]*26
        for c in s:
            counts[ord(c)-ord('a')] += 1
        return '-'.join(str(c) for c in counts)