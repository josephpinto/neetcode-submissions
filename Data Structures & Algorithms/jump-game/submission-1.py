class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = [False]*len(nums)
        result[0] = True

        for i,n in enumerate(nums):
            if n == 0 or not result[i]:
                continue
            for j in range(n):
                if i+j+1 < len(nums):
                    result[i+j+1] = True
        return result[-1]