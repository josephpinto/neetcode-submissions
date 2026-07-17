from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        queue = deque()
        num_fresh = 0
        # find rotten fruit
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        if num_fresh == 0:
            return 0
            
        while queue:
            time += 1
            queue_len = len(queue)
            for i in range(queue_len):
                sr,sc = queue.popleft()
                for nr,nc in directions:
                    r,c = sr+nr, sc+nc
                    if (r < 0 or r >= ROWS or
                        c < 0 or c >= COLS or
                        grid[r][c] != 1
                        ):
                        continue
                    num_fresh -= 1
                    if num_fresh == 0:
                        return time
                    grid[r][c] = 2
                    queue.append((r,c))
                



        return -1