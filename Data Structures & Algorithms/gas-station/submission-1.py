class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g-c for g,c in zip(gas,cost)]
        total = 0
        start = 0
        # always impossible to complete loop
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += diffs[i]
            if total < 0:
                start = i+1
                total = 0
        return start
        