from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultMap = defaultdict(list)
        for s in strs:
            resultMap[tuple(self.makeTable(s))].append(s)
        result = []
        return list(resultMap.values())

    
    def makeTable(self, str):
        res = [0]*26
        for c in str:
            index = ord(c)-ord('a')
            res[index] +=1
        return res
