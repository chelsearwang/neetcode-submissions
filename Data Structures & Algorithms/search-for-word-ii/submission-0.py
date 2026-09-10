class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.endOfWord = True
            node.word = word # store actual word

        # dfs
        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, trie_node):
            char = board[row][col]
            # check if char is valid next char in trie
            if char not in trie_node.children:
                return
            node = trie_node.children[char]
            # found a complete word
            if node.endOfWord:
                result.append(node.word)
                node.endOfWord = False
            
            board[row][col] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + dr
                new_col = col + dc
                if (0 <= new_row < rows and
                    0 <= new_col < cols and
                    board[new_row][new_col] != "#"):
                    dfs(new_row, new_col, node)
            board[row][col] = char # backtrack
        # start dfs from every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)
        return result














