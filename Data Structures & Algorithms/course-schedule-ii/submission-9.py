class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for c1,c2 in prerequisites:
            graph[c1].add(c2)

        path = []
        curr_path = []
        finished = set()

        def dfs(course):
            if course in curr_path:
                return False
            curr_path.append(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            curr_path.pop()
            graph[course] = []
            if course not in finished:
                path.append(course)
            finished.add(course)
            return True



        for c in range(numCourses):
            if not dfs(c):
                return []


        return path