class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            course_map[course].append(prereq)
        

        courses_taken = set()
        path = set()
        output = []


        def dfs(course):
            # cycle
            if course in path:
                return False
            # taken the course already
            if course in courses_taken:
                return True
                
            
            path.add(course)
            for prereq in course_map[course]:
                # can we take this prereq?
                if not dfs(prereq):
                    return False
            path.remove(course)
            output.append(course)
            courses_taken.add(course)
            return True
            
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output