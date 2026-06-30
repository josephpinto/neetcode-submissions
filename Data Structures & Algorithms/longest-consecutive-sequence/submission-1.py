from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLength = 1
        numsSet = set(nums)
        for n in nums:
            if n-1 in numsSet:
                continue
            currMax = 1
            currNum = n
            while currNum+1 in numsSet:
                currMax += 1
                currNum +=1
            maxLength = max(maxLength,currMax)
        return maxLength