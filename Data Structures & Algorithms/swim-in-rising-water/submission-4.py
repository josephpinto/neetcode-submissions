class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(grid[0][0],0,0)]

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        # want to find path with minimum max val
        # cost
        visited = set()
        visited.add((0,0))
        while min_heap:
            max_cost, r,c = heapq.heappop(min_heap)
            if r == ROWS-1 and c == COLS-1:
                return max_cost
            
            for nr, nc in directions:
                new_r, new_c = r+nr, c+nc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or (new_r,new_c) in visited:
                    continue
                new_max = max(max_cost, grid[new_r][new_c])
                visited.add((new_r,new_c))
                heapq.heappush(min_heap, (new_max, new_r,new_c))