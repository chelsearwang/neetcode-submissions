class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[course] = prerequisites needed for that course
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        visited = set() # courses checked, safe
        visiting = set() # # courses currently in the DFS path

        def dfs(course):
            if course in visited:
                return True
            if course in visiting: # cycle
                return False
            visiting.add(course)
            for prerequisite_course in graph[course]:
                if not dfs(prerequisite_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for course in range(len(graph)):
            if not dfs(course):
                return False
        return True