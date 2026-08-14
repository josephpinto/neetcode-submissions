class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        seen = set()
        def dfs(val,par):
            if val in seen:
                return False
            seen.add(val)
            for nei in graph[val]:
                if nei == par:
                    continue
                if not dfs(nei,val):
                    return False
            return True
        # cycle
        if not dfs(0,-1):
            return False
        return len(seen) == n
