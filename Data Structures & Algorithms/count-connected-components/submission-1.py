class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        
        seen = set()
        components = 0
        def dfs(node,parent):
            if node in seen:
                return
            seen.add(node)
            for child in graph[node]:
                dfs(child,node)
        
        for node in range(n):
            if node in seen:
                continue
            dfs(node,-1)
            components += 1
        return components


        