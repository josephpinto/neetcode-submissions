class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        res = 0
        for n in numsSet:
            # potential min
            if n-1 not in numsSet:
                curr = n
                curr_len = 1
                while curr+1 in numsSet:
                    curr_len += 1
                    curr +=1
                res = max(res, curr_len)
        return res