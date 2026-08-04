from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_length = 1
        nums_set = set(nums)
        for n in nums:
            # not a min
            if n-1 in nums_set:
                continue
            curr = 1
            curr_num = n
            while curr_num+1 in nums_set:
                curr += 1
                curr_num += 1
            max_length = max(max_length,curr)
        return max_length
