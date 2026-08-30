class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        posDiag = set() # same r+c
        cols = set()
        negDiag = set() # same r-c

        board = [['.']*n for _ in range(n)]
        def dfs(r):
            if r == n:
                # check copy logic
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if (c in cols or r+c in posDiag or r-c in negDiag):
                    continue
                board[r][c] = 'Q'
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)
                dfs(r+1)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)
                board[r][c] = '.'
        dfs(0)
        return res






        