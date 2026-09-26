class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                """
                ways = 0
                if i-1 >= 0:
                    ways += grid[i-1][j]
                if j-1 >= 0:
                    ways += grid[i][j-1]
                grid[i][j] = ways
                """
        # print(grid)
        return grid[m-1][n-1]

        """
        def recurse(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            return recurse(i+1, j) + recurse(i, j+1)
        return recurse(0, 0)
        """