class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(r,c, seen, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols 
            or (r,c) in seen or heights[r][c] < prev_height):
                return
            seen.add((r,c))
            for nr, nc in dirs:
                dfs(r+nr,c+nc, seen, heights[r][c])

        
        # pac
        for c in range(cols):
            dfs(0,c,pac,-1)
        for r in range(rows):
            dfs(r,0,pac,-1)

        # alt
        for c in range(cols):
            dfs(rows-1,c,atl,-1)
        for r in range(rows):
            dfs(r,cols-1,atl,-1)
        
        return [[r,c] for r,c in pac.intersection(atl)]




