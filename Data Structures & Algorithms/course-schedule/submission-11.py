class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for c1,c2 in prerequisites:
            graph[c1].add(c2)
        
        seen = set()
        finished = set()
        def dfs(course):
            if course in finished:
                return True
            if course in seen:
                return False
            seen.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            finished.add(course)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True