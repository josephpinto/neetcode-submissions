class TrieNode:
    def __init__(self):
        self.terminal = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.start = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.start
        for c in word:
            if c not in curr.children:
                new_node = TrieNode()
                curr.children[c] =  new_node
            curr = curr.children[c]
        curr.terminal = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, i):
            if i == len(word):
                return curr.terminal
            
            char = word[i]
            if char != '.':
                if char not in curr.children:
                    return False
                return dfs(curr.children[char],i+1)
            
            for child in curr.children:
                if dfs(curr.children[child],i+1):
                    return True
            return False
        return dfs(self.start,0)
            
                    
        
