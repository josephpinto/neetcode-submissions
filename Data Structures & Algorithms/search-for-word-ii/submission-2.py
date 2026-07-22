class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.terminal = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board), len(board[0])
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        # dummy node
        trie = TrieNode(-1)
        for word in words:
            self.addWord(word,trie)
        res = []
        visited = set()
        def dfs(r,c,trie_node,path):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited
            or board[r][c] not in trie_node.children):
                return
            new_node = trie_node.children[board[r][c]]
            new_word = path+board[r][c]
            if new_node.terminal:
                res.append(new_word)
                new_node.terminal = False
            
            for nr,nc in directions:
                visited.add((r,c))
                dfs(r+nr,c+nc,new_node,new_word)
                visited.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie,"")
        return res
            
            
    


    def addWord(self,word,trie):
        curr = trie
        for i,c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            
            curr = curr.children[c]
            if i == len(word)-1:
                curr.terminal = True
