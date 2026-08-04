class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] += 1
        res = 0
        curr_sum = 0
        for n in nums:
            curr_sum += n
            needed = curr_sum - k
            res += pre_sum[needed]
            pre_sum[curr_sum] += 1
        return res
