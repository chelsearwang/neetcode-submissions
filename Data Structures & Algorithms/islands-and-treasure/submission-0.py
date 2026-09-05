from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        queue = deque()
        # bfs from each treasure chest
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=INF):
                    continue    # invlaid neighbor cell
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))