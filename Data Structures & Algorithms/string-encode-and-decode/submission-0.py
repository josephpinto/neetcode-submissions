SEPERATOR = "#"
class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode length, seperator, string
        # 5//hello
        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append(SEPERATOR)
            result.append(string)
        print("result",result)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        while idx < len(s):
            endIdx = s.find(SEPERATOR, idx)
            length = int(s[idx:endIdx])
            print('length', length)
            result.append(s[endIdx+1:endIdx+1+length])
            idx += endIdx-idx+length+1
        return result



                



            # get length
            # append word