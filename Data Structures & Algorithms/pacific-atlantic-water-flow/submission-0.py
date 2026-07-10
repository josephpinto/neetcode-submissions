class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        seen_1 = set()
        seen_2 = set()
        ROWS,COLS = len(heights), len(heights[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        def dfs(r,c,prev_height,seen):
            if r < 0 or r >=ROWS or c < 0 or c >= COLS or (r,c) in seen or heights[r][c] < prev_height:
                return

            seen.add((r,c))

            for nr,nc in directions:
                dfs(r+nr,c+nc,heights[r][c],seen)
        
        for r in range(ROWS):
            dfs(r,0,-1,seen_1)

        for c in range(COLS):
            dfs(0,c,-1,seen_1)
        
        for r in range(ROWS):
            dfs(r,COLS-1,-1,seen_2)

        for c in range(COLS):
            dfs(ROWS-1,c,-1,seen_2)

        return list(seen_1.intersection(seen_2))