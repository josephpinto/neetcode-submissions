from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        queue = deque()
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0
        time = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                    # ignore OOB, rotten, visited - do I need visited?
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                    continue
                val = grid[r][c]
                grid[r][c] = 2
                visited.add((r,c))
                if val == 1:
                    num_fresh -= 1
                for nr, nc in directions:
                    queue.append((r+nr,c+nc))
            if num_fresh == 0:
                return time
            time += 1
            
        return -1
                    

















