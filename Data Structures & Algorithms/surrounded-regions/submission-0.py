class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            board[r][c] = 'B'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r+dr
                nc = c+dc
                if (nr<rows and nr>=0 and nc<cols and nc>=0 and board[nr][nc]=='O'):
                    dfs(nr, nc)
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols-1] == 'O':
                dfs(r, cols-1)
        for c in range(1, cols-1):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)
        # print(board)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'