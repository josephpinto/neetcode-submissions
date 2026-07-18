class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        found_sums = set()
        total_sum = sum(nums)
        if not total_sum % 2 == 0:
            return False
        target = total_sum/2
        for n in nums:
            if n == target: return True
            found_sums_c = found_sums.copy()
            for found_sum in found_sums_c:
                new_sum = found_sum + n
                if new_sum == target:
                    return True
                found_sums.add(new_sum)
            found_sums.add(n)
        return False