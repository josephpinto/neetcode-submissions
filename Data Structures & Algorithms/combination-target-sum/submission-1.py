class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i, target):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0 or i == len(nums):
                return
            # pick i
            curr.append(nums[i])
            dfs(i,target-nums[i])
            curr.pop()
            # continue
            dfs(i+1, target)


        dfs(0, target)
        return res