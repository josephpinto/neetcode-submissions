class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            sLen = len(string)
            res += str(sLen)
            res += '#'
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr_len = 0
        i = 0
        while i < len(s):
            hash_idx = s.find('#', i)
            length = int(s[i:hash_idx])
            string = s[hash_idx+1:hash_idx+1+length]
            res.append(string)
            i = hash_idx+length+1
        return res

            
