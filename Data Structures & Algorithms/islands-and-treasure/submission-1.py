class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        # bfs from each treasure

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        
        while queue:
            numPop = len(queue)
            for _ in range(numPop):
                # pop node, mark all valid non-init neibors with new val
                r,c = queue.popleft()
                
                for dr,dc in directions:
                    nr,nc = r+dr,dc+c
                    if nr<0 or nr==ROWS or nc<0 or nc==COLS or (nr,nc) in visited or grid[nr][nc] ==-1:
                        continue
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
                    visited.add((nr,nc))
    