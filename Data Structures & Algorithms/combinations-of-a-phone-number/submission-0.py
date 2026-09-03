class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dictionary mapping each digit to corresponding letters?
        result = []
        combo = []
        mydict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(start):
            if start == len(digits):
                result.append("".join(combo))
                return
            digit = digits[start]
            letters = mydict[digit]
            for letter in letters:
                combo.append(letter)
                backtrack(start+1)
                combo.pop()

        if not digits:
            return []

        backtrack(0)
        return result