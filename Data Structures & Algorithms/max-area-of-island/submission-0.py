class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        ROWS,COLS = len(grid), len(grid[0])
        max_area = 0

        def getArea(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            result = 1
            grid[r][c] = 0
            for nr,nc in directions:
                result += getArea(r+nr,c+nc)
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, getArea(r,c))



        return max_area