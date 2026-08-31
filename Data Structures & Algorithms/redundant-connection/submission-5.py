class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for n1,n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        cycle = set()
        visit = set()
        cycleStart = -1
        def dfs(node,par):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True

            visit.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1,0)

        for n1,n2 in edges[::-1]:
            if n1 in cycle and n2 in cycle:
                return [n1,n2]
            
            