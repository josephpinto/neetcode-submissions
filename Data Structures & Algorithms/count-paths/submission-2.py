class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        grid[-1][-1] = 1

        ROWS,COLS = m,n
        def isOOB(r,c):
            return r < 0 or r >= ROWS or c < 0 or c >= COLS
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if not isOOB(r+1,c):
                    grid[r][c] += grid[r+1][c]
                if not isOOB(r,c+1):
                    grid[r][c] += grid[r][c+1]
        return grid[0][0]
        

                