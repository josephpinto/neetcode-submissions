class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        # mark all places as safe going inward
        # replace all non-safe with X
        # mark safe as 0

        def dfs(i,j):
            if i<0 or i==rows or j<0 or j==cols or board[i][j] == 'X' or board[i][j] == '#':
                return
            board[i][j] = '#'
            for nr,nc in dirs:
                dfs(i+nr,j+nc)
        
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[rows-1][c] == 'O':
                dfs(rows-1,c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
