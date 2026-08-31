class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        # track max cost of entire path
        heap = [(grid[0][0],0,0)]
        visit = set()
        while heap:
            max_cost, r,c = heapq.heappop(heap)
            if r == ROWS-1 and c == COLS-1:
                return max_cost
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if nr<0 or nr == ROWS or nc<0 or nc == COLS or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(heap,(max(max_cost, grid[nr][nc]),nr,nc))
        return

        

