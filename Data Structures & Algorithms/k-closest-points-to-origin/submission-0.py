import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        heap = []

        for point in points:
            x,y = point
            distance = math.sqrt(x*x+y*y)
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]
        # k closest - min distance. max heap of size k


    