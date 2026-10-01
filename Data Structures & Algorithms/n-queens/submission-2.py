class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set() # r+c
        negDiag = set() # r-c

        board = [['.']*n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append([''.join(r) for r in board])
                return
            for c in range(n):
                # try placing in each col in the row
                if c not in col and (r-c) not in negDiag and r+c not in posDiag:
                    board[r][c] = 'Q'
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    dfs(r+1)
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    board[r][c] = '.'
        dfs(0)
        return res