class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            curr_num = nums[i]
            while i<len(nums) and nums[i] == curr_num:
                i += 1
            dfs(i)
        dfs(0)
        return res