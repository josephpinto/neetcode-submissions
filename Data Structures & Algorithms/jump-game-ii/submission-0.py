class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1

        l=r=0
        jumps = 0
        while r < goal:
            farthest = r
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            jumps += 1

        return jumps