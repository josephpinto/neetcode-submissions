class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        required_f = [0]*26
        curr_f = [0]*26

        for c in s1:
            required_f[ord(c)-ord('a')] += 1
        
        for init_idx in range(len(s1)):
            char = s2[init_idx]
            curr_f[ord(char)-ord('a')] += 1
            if curr_f == required_f:
                return True
        
        for curr_idx in range(1, len(s2)-len(s1)+1):
            curr_f[ord(s2[curr_idx-1])-ord('a')] -= 1
            new_char = s2[curr_idx+len(s1)-1]
            curr_f[ord(new_char)-ord('a')] += 1
            if curr_f == required_f:
                return True
        return False