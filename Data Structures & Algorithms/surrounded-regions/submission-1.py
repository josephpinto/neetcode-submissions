class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        def dfs(r,c):
            if (r<0 or r >=ROWS or c<0 or c>=COLS
                or board[r][c] != 'O'):
                return
            board[r][c] = '#'
            for nr,nc in directions:
                dfs(nr+r,nc+c)
        
        border_nodes = []
        for r in range(ROWS):
            if board[r][0] == 'O':
                border_nodes.append((r,0))
            if board[r][COLS-1] == 'O':
                border_nodes.append((r,COLS-1))
        
        for c in range(COLS):
            if board[0][c] == 'O':
                border_nodes.append((0,c))
            if board[ROWS-1][c] == 'O':
                border_nodes.append((ROWS-1,c))
        
        for r,c in border_nodes:
            dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'


