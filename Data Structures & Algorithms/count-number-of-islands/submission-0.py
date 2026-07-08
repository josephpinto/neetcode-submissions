class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def search(r,c):
            nonlocal res
            if r < 0 or r >=ROWS or c < 0 or c >=COLS or grid[r][c] == '0':
                return
            res += 1
            sink(r,c)

        def sink(r,c):
            if r < 0 or r >=ROWS or c < 0 or c >=COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for nr,nc in directions:
                sink(r+nr,c+nc)
            

        for r in range(ROWS):
            for c in range(COLS):
                search(r,c)




        return res