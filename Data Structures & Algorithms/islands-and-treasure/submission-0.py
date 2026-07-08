from collections import deque

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
        queue = deque()

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        curr_dist = 0
        while queue:
            # process all neighbours of all gates
            for _ in range(len(queue)):
                
                r,c = queue.popleft()
                if r < 0 or r >=ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r,c) in visited:
                    continue
                # in bounds, new node
                grid[r][c] = curr_dist
                visited.add((r,c))
                for nr, nc in directions:
                    queue.append((r+nr, c+nc))
            curr_dist += 1
        