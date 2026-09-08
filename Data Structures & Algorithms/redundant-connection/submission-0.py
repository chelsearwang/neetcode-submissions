class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b: # already connected
                return [a, b]

            parent[root_a] = root_b # currently disconnected, union components

        return []