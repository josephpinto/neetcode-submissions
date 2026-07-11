class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:
            course_map[c].append(p)
        
        curr_path = set()
        
        def dfs(course):
            if course in curr_path:
                return False
            curr_path.add(course)
            for pre in course_map[course]:
                if not dfs(pre): return False
            curr_path.remove(course)
            return True
            


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
            
