class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = s.lower()
        SAlNum = ''.join(filter(lambda c: c.isalnum(),sLower))
        for i in range(len(SAlNum)//2):
            print(SAlNum[i],SAlNum[-i-1])
            if SAlNum[i] != SAlNum[-i-1]:
                return False
        return True
