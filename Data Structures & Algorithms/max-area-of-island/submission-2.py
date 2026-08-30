class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def sink(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            res = 1
            for nr,nc in directions:
                res += sink(r+nr,c+nc)
            return res


        maxx = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxx = max(maxx,sink(r,c))
        return maxx