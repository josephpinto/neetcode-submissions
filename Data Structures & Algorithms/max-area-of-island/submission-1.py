class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        visit = set()
        def dfs(i,j):
            if( i < 0 or i >= rows or j < 0 or j >= cols
            or grid[i][j] == 0):
                return 0
            # found a 1
            res = 1
            grid[i][j] = 0
            for nr,nc in directions:
                res += dfs(i+nr, j+nc)
            return res
        maxx = 0
        for r in range(rows):
            for c in range(cols):
                maxx = max(maxx, dfs(r,c))
        return maxx


            