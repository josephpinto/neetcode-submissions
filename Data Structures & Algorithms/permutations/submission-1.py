class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        remaining = set(nums)
        curr = []
        res = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
            remainingCopy = remaining.copy()
            for n in remainingCopy:
                remaining.remove(n)
                curr.append(n)
                dfs()
                curr.pop()
                remaining.add(n)
            return
        dfs()
        return res