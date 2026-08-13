class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        res = 1
        for i,n in enumerate(nums):
            if n-1 in num_set:
                continue
            curr = n
            curr_res = 0
            while curr in num_set:
                curr_res += 1
                curr += 1
            res = max(res, curr_res)
        return res
