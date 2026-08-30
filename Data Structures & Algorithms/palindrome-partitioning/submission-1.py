class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(start_curr,i):
            if i == len(s):
                curr_len = 0
                for part in curr:
                    curr_len+=len(part)
                if curr_len == len(s):
                    res.append(curr[:])
                return
            # start a new part
            new_part = s[start_curr:i+1]
            if self.isPal(new_part):
                curr.append(new_part)
                dfs(i+1,i+1)
                curr.pop()
            # continue current part
            dfs(start_curr,i+1)

        dfs(0,0)
        return res

    def isPal(self, s):
        l,r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True