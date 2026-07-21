from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        seen = set()
        for u,v,t in times:
            graph[u].add((v,t))
        heap = [(0,k)]
        max_time = 0
        while heap:
            time_elapsed, node  = heapq.heappop(heap)
            if node in seen: continue
            max_time = max(max_time, time_elapsed)
            for v,t in graph[node]:
                new_time = time_elapsed+t
                heapq.heappush(heap,(time_elapsed+t,v))
            seen.add(node)
            if len(seen) == n:
                return max_time
        return -1


        