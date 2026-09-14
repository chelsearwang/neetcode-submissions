import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]  # (cost, row, col)
        visited = set() # (row, col)

        while heap:
            cost, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == n - 1 and col == n - 1:
                return cost

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]: 
                nr = row + dr 
                nc = col + dc 
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited: 
                    new_cost = max(cost, grid[nr][nc])
                    heapq.heappush(heap, (new_cost, nr, nc))