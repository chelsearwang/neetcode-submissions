class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles
        if len(edges) != n-1:
            return False

        graph = [[] for _ in range(n)]
        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        dfs(0)
        return len(visited) == n