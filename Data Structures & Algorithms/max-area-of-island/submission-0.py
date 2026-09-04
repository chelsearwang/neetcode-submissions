class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        curArea = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            nonlocal curArea
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited):
                return
            visited.add((r ,c))
            curArea += 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    maxArea = max(curArea, maxArea)
                    curArea = 0
        return maxArea