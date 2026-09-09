class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.endOfWord
            char = word[index]
            if char != ".":
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
            else:
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
        return dfs(self.root, 0)

