from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs starting at every rotten fruit
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0 # count fresh fruit
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        mins = 0
        while queue and fresh > 0:
            q_len = len(queue)
            for i in range(q_len):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if (nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=1):
                        continue    # invlaid neighbor cell
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            mins += 1
        if fresh != 0:
            return -1
        return mins