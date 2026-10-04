class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while heap and len(heap) > 1:
            x,y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x == y:
                continue
            if x > y:
                heapq.heappush(heap,-(x-y))
            else:
                heapq.heappush(heap,-(y-x))
        return -heap[0] if heap else 0