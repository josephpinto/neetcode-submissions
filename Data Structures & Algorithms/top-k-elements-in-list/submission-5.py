class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap
        heap = []
        counts = Counter(nums)
        for n in counts:
            count = counts[n]
            heapq.heappush(heap, (count,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for _, n in heap]
