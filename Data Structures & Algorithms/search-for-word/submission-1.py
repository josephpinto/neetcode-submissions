class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])

        visit = set()
        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def dfs(word_idx,i,j):
            if word_idx == len(word):
                return True
            if i<0 or i == rows or j < 0 or j == cols or (i,j) in visit:
                return False
            if board[i][j] != word[word_idx]:
                return False

            char = board[i][j]
            visit.add((i,j))
            
            for nr,nc in dirs:
                if dfs(word_idx+1,i+nr,j+nc):
                    return True
            visit.remove((i,j))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if dfs(0,i,j):
                    return True
        return False
            
            