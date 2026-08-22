class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 1
        for n in nums:
            if n-1 in nums_set:
                continue
            curr = n
            curr_res = 0
            while curr in nums_set:
                curr += 1
                curr_res += 1
            res = max(res,curr_res)
        return res
            

