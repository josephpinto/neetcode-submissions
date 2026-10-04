class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(r,c):
            if (r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]!=1):
                return 0
            grid[r][c] = 0
            res = 1
            for nr,nc in dirs:
                res += dfs(r+nr,c+nc)
            return res

        maxx = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxx = max(maxx, dfs(r,c))
        return maxx