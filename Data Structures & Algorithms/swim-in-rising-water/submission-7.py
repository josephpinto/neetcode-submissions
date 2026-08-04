class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # find the path with the minimum max num
        heap = [(grid[0][0],0,0)]

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        visited = set()
        while heap:
            max_path_val, r,c = heapq.heappop(heap)
            if r == ROWS-1 and c == COLS-1:
                return max_path_val
            for nr,nc in directions:
                new_r, new_c = r+nr, c+nc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or (new_r,new_c) in visited:
                    continue
                visited.add((new_r,new_c))
                # BFS, record max of path
                heapq.heappush(heap,(max(max_path_val,grid[new_r][new_c]),new_r,new_c))

            