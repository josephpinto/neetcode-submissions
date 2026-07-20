class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_nums = [False,False,False]
        cand_indexes = []
        for x,y,z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0]:
                found_nums[0] = True
            if y == target[1]:
                found_nums[1] = True
            if z == target[2]:
                found_nums[2] = True
        for res in found_nums:
            if not res:
                return False

        return True
