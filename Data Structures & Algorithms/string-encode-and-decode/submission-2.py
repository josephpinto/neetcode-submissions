SEPERATOR = '#'
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+=str(len(s))
            res += SEPERATOR
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            next_sep = s.find(SEPERATOR,i)
            next_len = int(s[i:next_sep])
            i += len(str(next_len)) + 1
            res.append(s[i:i+next_len])
            i+=next_len
        return res