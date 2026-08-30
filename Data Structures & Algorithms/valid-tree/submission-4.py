class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is connected, acyclic
        graph = defaultdict(set)

        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        seen = set()

        def dfs(node,prev):
            if node in seen:
                return False
            seen.add(node)
            for child in graph[node]:
                if child == prev:
                    continue
                if not dfs(child,node):
                    return False
            return True
            


        if not dfs(0,-1):
            return False
        # fully connected
        return len(seen) == n