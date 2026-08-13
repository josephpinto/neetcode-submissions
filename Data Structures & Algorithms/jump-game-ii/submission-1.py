class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        l, r = 0,0
        jumps = 0
        while r < goal:
            farthest_jump = r
            for i in range(l, r+1):
                farthest_jump = max(farthest_jump, i+nums[i])
            l = r+1
            r = farthest_jump
            jumps += 1
        return jumps
