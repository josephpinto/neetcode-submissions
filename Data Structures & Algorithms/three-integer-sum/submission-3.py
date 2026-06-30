class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        resultSet = set()
        for idx, target in enumerate(sortedNums):
            negTarget = -target
            l,r = idx+1, len(sortedNums)-1
            while l<r:
                currSum = sortedNums[l] + sortedNums[r]
                if currSum == negTarget:
                    resultSet.add((target, sortedNums[l], sortedNums[r]))
                    l += 1
                    r -= 1
                    continue
                if currSum < negTarget:
                    l += 1
                if currSum > negTarget:
                    r -= 1
                
        return [[x,y,z] for x,y,z in resultSet]
