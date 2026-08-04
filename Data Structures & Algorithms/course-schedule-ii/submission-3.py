class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for c1,c2 in prerequisites:
            graph[c1].add(c2)
        # already processed, safe to return True
        courses_taken = set()
        # current stack
        path = set()
        
        res = []
        def dfs(course):
            if course in courses_taken:
                return True
            if course in path:
                return False
            path.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            # post order add course
            courses_taken.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res