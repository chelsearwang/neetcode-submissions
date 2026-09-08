from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            # try changing each char
            for i in range(len(word)):
                # try every char
                for char in "abcdefghijklmnopqrstuvwxyz":
                    candidate = word[:i] + char + word[i + 1:]
                    # if valid and unvisitd, add to bfs
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, dist + 1))
        return 0
        """
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
        """
