class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        # find all rotten fruit
        rotten = []
        num_fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    num_fresh += 1
        if num_fresh == 0:
            return 0
        if not rotten:
            return -1
        
        queue = deque(rotten)
        t = 0
        while queue:
            t += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    num_fresh -= 1
                    if num_fresh == 0:
                        return t
                    queue.append((nr,nc))
            # processed one minute
        return -1