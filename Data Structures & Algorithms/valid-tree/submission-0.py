class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node: [] for node in range(n) }

        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        
        seen = set()

        def dfs(node,parent):
            if node in seen:
                return False
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor,node): return False
            return True

        
        # captured all nodes
        return dfs(0,-1) and len(seen) == n