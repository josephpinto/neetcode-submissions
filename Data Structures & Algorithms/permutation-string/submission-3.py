class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        required = [0]*26
        s1_chars = set(s1)
        for c in s1:
            required[ord(c)-ord('a')] += 1
        
        curr_freqs =[0]*26

        for init_index in range(len(s1)):
            char = s2[init_index]
            curr_freqs[ord(char)-ord('a')] += 1
            if curr_freqs == required:
                return True
        for i in range(1,len(s2)-len(s1)+1):
            curr_freqs[ord(s2[i-1])-ord('a')] -= 1
            new_char = s2[i+len(s1)-1]
            curr_freqs[ord(new_char)-ord('a')] += 1
            if curr_freqs == required:
                return True
                
        return False
                
            