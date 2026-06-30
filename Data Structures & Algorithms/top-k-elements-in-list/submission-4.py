from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        # make maxHeap by count (O(n))
        # pop first k elements off of the heap (nlogn)

        heap = []
        for val,count in counts.items():
            heap.append((-count,val))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]