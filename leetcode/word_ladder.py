from collections import defaultdict
from typing import List


# A shortest path problem that can solved with BFS
# The main challenge is to construct the Adjecency list
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + '*' + word[i+1:]
                adj[p].append(word)

        visited = set([beginWord])
        q = [beginWord]
        res = 1

        while q:
            for i in range(len(q)):
                word = q.pop(0)

                if word == endWord:
                    return res

                for i in range(len(word)):
                    p = word[:i] + '*' + word[i+1:]
                    for n in adj[p]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
            res += 1

        return 0
