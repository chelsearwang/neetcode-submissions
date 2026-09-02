class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combo = []
        def backtrack(l, r): # l and r are num of open/closing paretheses available
            if l == 0 and r == 0:
                result.append("".join(combo))
            if l > 0: # explore combos with "("
                combo.append("(")
                backtrack(l-1, r+1)
                combo.pop()
            if r > 0: # explore combos with ")"
                combo.append(")")
                backtrack(l, r-1)
                combo.pop()

        backtrack(n, 0)
        return result