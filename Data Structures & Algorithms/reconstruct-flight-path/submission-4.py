from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        for key in graph:
            graph[key].sort()
        res = ["JFK"]

        def dfs(curr_res):
            nonlocal res
            if len(curr_res) == len(tickets) + 1:
                res = curr_res
                return True
            curr = curr_res[-1]
            if not graph[curr]: return False
            cands = graph[curr].copy()
            for dest in cands:
                print('dest', dest)
                print('curr', curr)
                graph[curr].remove(dest)
                if dfs(curr_res+[dest]): return True
                else: 
                    graph[curr].append(dest)
                    graph[curr].sort()
            # should never happen
            return False
        dfs(["JFK"])
        return res
            