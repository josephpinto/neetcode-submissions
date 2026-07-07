class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colHits = set()
        posDiag = set() # same r-c
        negDiag = set() # same r+c
        res = []

        board = [["."]*n for _ in range(n)]
        print(board)

        def dfs(r):
            if r == n:
                # maybe need to copy
                res.append(["".join(row) for row in board])
            for col in range(n):
                if col not in colHits and r-col not in posDiag and r+col not in negDiag:
                    colHits.add(col)
                    posDiag.add(r-col)
                    negDiag.add(r+col)
                    board[r][col] = 'Q'
                    dfs(r+1)
                    colHits.remove(col)
                    posDiag.remove(r-col)
                    negDiag.remove(r+col)
                    board[r][col] = '.'
            

        dfs(0)

        return res