class TrieNode:
    def __init__(self):
        self.children={}
        self.terminal=False

class PrefixTree:

    def __init__(self):
        self.start = TrieNode()

    def insert(self, word: str) -> None:
        node = self.start
        for i,c in enumerate(word):
            if c not in node.children:
                newNode = TrieNode()
                node.children[c] = newNode
            node = node.children[c]
            if i == len(word)-1:
                node.terminal = True


    def search(self, word: str) -> bool:
        node = self.start
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.start
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        