from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        visited = set()
        cycleNodes = set()
        cycle_start = None
        def dfs(node,par):
            nonlocal cycle_start
            if node in visited:
                cycle_start = node
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    # reached front of cycle again
                    cycleNodes.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True
        
        dfs(edges[0][0],-1)
        print(cycleNodes)
        for x,y in edges[::-1]:
            if x in cycleNodes and y in cycleNodes:
                return [x,y]