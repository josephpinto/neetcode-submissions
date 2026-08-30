class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return
            # choose i
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            # skip i
            dfs(i+1)
        dfs(0)
        return res