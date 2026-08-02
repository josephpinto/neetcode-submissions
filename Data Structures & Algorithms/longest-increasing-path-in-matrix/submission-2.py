class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(10000000)
        cache = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            
            curr_num = matrix[r][c]
            lip = 1
            for nr,nc in directions:
                new_r, new_c = nr+r,nc+c
                if (new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS 
                or matrix[new_r][new_c] <= curr_num):
                    continue
                lip = max(lip, 1+ dfs(new_r,new_c))
            cache[(r,c)] = lip
            return lip

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)

        return max(list(cache.values()))



