class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start_curr_part, i, curr_parts):
            if i == len(s):
                len_sum = 0
                for partition in curr_parts:
                    len_sum += len(partition)
                if len_sum == len(s):
                    res.append(curr_parts.copy())
                return


            
            # try partition at i
            new_part = s[start_curr_part:i+1]
            if self.isPal(new_part):
                curr_parts.append(new_part)
                dfs(i+1,i+1,curr_parts)
                curr_parts.pop()
            # continue without partition
            dfs(start_curr_part,i+1,curr_parts)

        dfs(0,0,[])

        return res
    


    def isPal(self,s):
        l,r = 0, len(s)-1

        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True