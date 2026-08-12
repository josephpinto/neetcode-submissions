class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []

        def dfs(rows_left,cols_left, r,c, dr,dc):
            if rows_left == 0 or cols_left == 0:
                return
            for i in range(cols_left):
                r+=dr
                c+=dc
                res.append(matrix[r][c])
            dfs(cols_left,rows_left-1,r,c,dc,-dr)

        
        dfs(rows,cols,0,-1,0,1)

        return res