class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(10000000)

        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        visited = set()
        cache = {}
        def dfs(r,c, prev):
            if (r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or matrix[r][c] <= prev):
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            visited.add((r,c))
            local_max = 1
            for nr,nc in dirs:
                local_max = max(local_max, 1+ dfs(r+nr,c+nc, matrix[r][c]))
            visited.remove((r,c))
            cache[(r,c)] = local_max
            return local_max



        maxx = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxx = max(maxx, dfs(r,c,-1))

        return maxx