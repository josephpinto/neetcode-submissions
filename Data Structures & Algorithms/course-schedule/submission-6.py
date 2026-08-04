class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for c1, c2 in prerequisites:
            graph[c1].add(c2)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True