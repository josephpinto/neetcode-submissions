class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            num = nums[i]
            while i<len(nums) and nums[i] == num:
                i+=1
            dfs(i)



        dfs(0)
        return res