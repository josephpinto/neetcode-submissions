class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
    
        seen = set()
        def dfs(node,parent):
            # cycle
            if node in seen:
                return False
            seen.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                if not dfs(child,node): 
                    return False
            return True
            
        return dfs(0,-1) and len(seen) == n

