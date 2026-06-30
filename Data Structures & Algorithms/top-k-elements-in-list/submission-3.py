from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        result = []
        freqTable = [[] for _ in range(len(nums)+1)]

        for v,count in counts.items():
            freqTable[count].append(v)
        
        for bucket in reversed(freqTable):
            for num in bucket:
                if(len(result)) == k:
                    return result
                result.append(num)
        return result
        
            