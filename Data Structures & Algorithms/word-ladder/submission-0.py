from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_graph = defaultdict(set)
        
        # initial word
        for word in wordList:
            if self.oneOff(beginWord, word):
                word_graph[beginWord].add(word)
        
        for key in wordList:
            for word in wordList:
                if word == key:
                    continue
                if self.oneOff(key,word):
                    word_graph[key].add(word)
        
        queue = deque([beginWord])
        steps = 0
        visited = set()
        while queue:
            steps +=1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps
                for nei in word_graph[word]:
                    if nei in visited: 
                        continue
                    queue.append(nei)
                visited.add(word)
        return 0

    
    
    def oneOff(self, s,t):
        foundDiff = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if foundDiff: return False
                foundDiff = True
        return True