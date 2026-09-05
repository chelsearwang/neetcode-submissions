class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(r, c, visited):
            # mark current cell
            visited.add((r, c))

            # explore 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                # check if valid neighbor
                if (nr>=0 and nr<rows and nc>=0 and nc<cols 
                    and (nr, nc) not in visited
                    and heights[nr][nc]>=heights[r][c]):
                    dfs(nr, nc, visited)
        # call dfs from border cells            
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)
        # check which coords are in both pac and atl
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result