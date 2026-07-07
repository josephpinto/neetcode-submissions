import heapq

class MedianFinder:

    def __init__(self):
        # N/2 smallest numbers
        self.max_heap = []
        # N/2 biggest numbers
        self.min_heap = []    

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) - len(self.min_heap) > 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)

    def findMedian(self) -> float:
        if not self.max_heap and not self.min_heap:
            return 0
        if not self.max_heap:
            return self.min_heap[0]
        if not self.min_heap:
            return -self.max_heap[0]
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        
        