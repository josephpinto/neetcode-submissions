class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x,y in points:
            dist.append([x*x+y*y,[x,y]])
        heapq.heapify(dist)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(dist)[1])
        return res