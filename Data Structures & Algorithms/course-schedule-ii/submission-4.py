class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for c1,c2 in prerequisites:
            graph[c1].add(c2)

        finished = set()
        res = []
        visiting = set()
        def dfs(course):
            if course in finished:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            finished.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
        