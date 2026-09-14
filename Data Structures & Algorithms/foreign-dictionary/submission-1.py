from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word: # account fo revery char
                indegree[char] = 0

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            found_difference = False

            for j in range(min_len):
                if word1[j] != word2[j]:    # diff
                    char1 = word1[j]
                    char2 = word2[j]
                    if char2 not in graph[char1]:
                        graph[char1].add(char2) # char1 -> char2
                        indegree[char2] += 1
                    found_difference = True
                    break
            # invalid prefix case
            if not found_difference and len(word1) > len(word2):
                return ""
        
        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree): # cycle 
            return ""

        return "".join(result)