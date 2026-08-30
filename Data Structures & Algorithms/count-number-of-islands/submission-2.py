class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        dirs = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]

        count = 0
        def sink(r,c):
            if r<0 or r == rows or c<0 or c == cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for nr,nc in dirs:
                sink(r+nr,c+nc)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    sink(r,c)
                    count += 1
        return count





