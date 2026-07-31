import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        res = []
        for q in queries:
            minHeap = []
            i = 0
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                res.append(minHeap[0][0])
            else:
                res.append(-1)
        return res
