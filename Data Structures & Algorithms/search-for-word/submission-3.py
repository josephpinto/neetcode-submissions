class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board), len(board[0])
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(r,c,i,visit):
            if i == len(word):
                return True
            if(r<0 or r==ROWS or c<0 or c == COLS or (r,c) in visit or board[r][c]!=word[i]):
                return False
            visit.add((r,c))
            for nr,nc in dirs:
                if dfs(r+nr,c+nc,i+1,visit):
                    return True
            visit.remove((r,c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0,set()):
                    return True
        return False