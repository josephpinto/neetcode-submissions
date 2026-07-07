class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]

        def dfs(word_idx, pos):
            r,c = pos
            if word_idx == len(word):
                return True
            # OOB or already found or visited
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or 
            board[r][c] == '#' or board[r][c] != word[word_idx]):
                return False
            
            
            
            board[r][c] = '#'
            # explore
            for n_r, n_c in directions:
                new_r, new_c = r+n_r,c+n_c
                if dfs(word_idx+1, (new_r,new_c)):
                    return True
            board[r][c] = word[word_idx]


        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(0, (row,col)):
                    return True
        return False
