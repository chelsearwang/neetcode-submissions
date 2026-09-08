from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def differs_by_one(word1, word2):
            if len(word1) != len(word2):
                return False
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            if count == 1:
                return True
            return False
        queue = deque() # store (word, distance)
        visited = set()

        found = False
        for word in wordList:
            if endWord == word:
                found = True
        if not found:
            return 0

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for next_word in wordList:
                if next_word not in visited and differs_by_one(word, next_word):
                    visited.add(next_word)
                    queue.append((next_word, dist + 1))
        return 0
