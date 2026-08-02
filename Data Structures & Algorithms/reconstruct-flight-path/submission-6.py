from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        res_length = len(tickets) + 1
        for source, dst in tickets:
            if source not in graph:
                graph[source] = defaultdict(int)
            graph[source][dst] += 1

        res = []
        def dfs(curr_path, graph):
            nonlocal res
            if len(curr_path) == res_length:
                res = curr_path
                return
            if res: return
            curr_node = curr_path[-1]
            if curr_node not in graph: return
            neighbors = graph[curr_node]
            for nei in sorted(neighbors):
                if neighbors[nei] == 0:
                    continue
                neighbors[nei] -= 1
                dfs(curr_path + [nei], graph)
                neighbors[nei] += 1
            
        
        dfs(["JFK"], graph)

        return res
            