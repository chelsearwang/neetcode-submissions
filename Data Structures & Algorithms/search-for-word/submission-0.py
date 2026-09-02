class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtrack(r, c, i):
            # Current cell doesn't match
            if board[r][c] != word[i]:
                return False
            # Successfully matched the entire word
            if i == len(word) - 1:
                return True
            
            visited.add((r, c))
            # Down
            if r < rows - 1 and (r + 1, c) not in visited:
                if backtrack(r + 1, c, i + 1):
                    return True
            # Up
            if r > 0 and (r - 1, c) not in visited:
                if backtrack(r - 1, c, i + 1):
                    return True
            # Right
            if c < cols - 1 and (r, c + 1) not in visited:
                if backtrack(r, c + 1, i + 1):
                    return True
            # Left
            if c > 0 and (r, c - 1) not in visited:
                if backtrack(r, c - 1, i + 1):
                    return True

            # Undo this cell before returning
            visited.remove((r, c))
            return False
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    result = backtrack(r, c, 0)
                    if result:
                        return True
        return False