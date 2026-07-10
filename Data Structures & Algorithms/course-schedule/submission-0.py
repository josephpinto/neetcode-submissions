from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {course: set() for course in range(numCourses)}
        for course, prereq in prerequisites:
                nodes[course].add(prereq)
        
        def dfs(path,curr_course):
            if curr_course in path:
                return False
            path.add(curr_course)
            for prereq in nodes[curr_course]:
                if not dfs(path,prereq): return False
            path.remove(curr_course)
            return True
            

        
        for course in nodes:
            if not dfs(set(),course):
                return False
        return True
            
