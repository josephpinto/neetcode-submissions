class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(path, i):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(path, i+1)
            path.pop()
            original_num = nums[i]
            while i < len(nums) and nums[i] == original_num:
                i += 1
            dfs(path,i)


        dfs([],0)
        return res