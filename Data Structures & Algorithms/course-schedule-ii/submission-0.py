class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        visiting = set()
        visited = set()
        result = []

        def dfs(course):
            if course in visited: 
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            result.append(course) # add to result after checkign prereqs
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        