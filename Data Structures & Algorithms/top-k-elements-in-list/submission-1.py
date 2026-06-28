from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-count, val) for val,count in counts.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k) ]
        
            