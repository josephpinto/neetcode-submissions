class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        graph = defaultdict(list)
        seen = set()
        for u,v,d in times:
            graph[u].append((d,v))
        
        minHeap = [(0,k)]
        t = 0
        while minHeap:
            # mark node seen
            # queue children with time to receieve = t+delay
            ttr, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            t = ttr
            if len(seen) == n:
                return t
            for delay,nei in graph[node]:
                heapq.heappush(minHeap, (t+delay,nei))
        return -1


        