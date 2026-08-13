class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [
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
        num_rotten = len(queue)
        if num_fresh == 0:
            return 0
        if num_rotten == 0:
            return -1

        time = 0
        visited = set(list(queue.copy()))
        while queue:
            num_to_pop = len(queue)
            for _ in range(num_to_pop):
                r,c = queue.popleft()
                visited.add((r,c))
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    num_fresh -= 1
                if num_fresh == 0:
                    return time
                for nr,nc in dirs:
                    new_r, new_c = nr+r, nc+c
                    if (new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS
                        or grid[new_r][new_c] == 0 or (new_r,new_c) in visited                    
                    ):
                        continue
                    queue.append((new_r,new_c))
            time += 1
        return -1