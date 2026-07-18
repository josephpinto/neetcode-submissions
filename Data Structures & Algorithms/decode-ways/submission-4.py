class Solution:
    def numDecodings(self, s: str) -> int:
        one_back, two_back = 1,1
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                # stop early - no way to decode the string from this point
                one_back, two_back = 0, one_back
                continue
            # this is a valid digit, count decodings of s[i+1:]
            curr = one_back

            if (i+1 < len(s) and (s[i]== '1' or (s[i]=='2' and s[i+1] in "0123456"))):
                curr += two_back
            one_back,two_back = curr, one_back
        return one_back
