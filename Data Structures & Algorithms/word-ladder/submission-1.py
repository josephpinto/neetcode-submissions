class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)

        for word in wordList:
            if self.isOneOff(beginWord, word):
                graph[beginWord].add(word)
        for word in wordList:
            for w2 in wordList:
                if word == w2:
                    continue
                if self.isOneOff(word,w2):
                    graph[word].add(w2)
        
        queue = deque([beginWord])
        visit = set([beginWord])
        res = 1
        found = False
        while queue:
            # explore frontier
            for _ in range(len(queue)):
                next_word = queue.popleft()
                if next_word == endWord:
                    return res
                for nei in graph[next_word]:
                    if nei in visit:
                        continue
                    queue.append(nei)
                    visit.add(nei)
            res += 1




        return 0









    def isOneOff(self,s,t):
        if len(s) != len(t):
            return False
        diff = False
        for c1,c2 in zip(s,t):
            if c1 != c2:
                if diff:
                    return False
                diff = True
        return True