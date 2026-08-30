class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for c1,c2 in prerequisites:
            graph[c1].append(c2)
        
        res = list()
        finished = set()
        curr_path = set()
        def dfs(course):
            if course in curr_path:
                return False
            curr_path.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            curr_path.remove(course)
            graph[course] = []
            if course not in finished:
                res.append(course)
                finished.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return list(res)





        