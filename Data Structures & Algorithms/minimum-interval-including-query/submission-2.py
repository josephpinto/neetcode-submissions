class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = []
        for q in queries:
            heap = []
            i = 0
            while i < len(intervals) and intervals[i][0] <= q:
                s,e = intervals[i][0], intervals[i][1]
                heapq.heappush(heap, (e-s+1,e))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res.append(heap[0][0])
            else:
                res.append(-1)
        return res
            