class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()

        graph = defaultdict(set)
        for n1,n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)

            for nei in graph[node]:
                dfs(nei)
        num_comp = 0
        for node in range(n):
            if node in seen:
                continue
            dfs(node)
            num_comp += 1
        return num_comp