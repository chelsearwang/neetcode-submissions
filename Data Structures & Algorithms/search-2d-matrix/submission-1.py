class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[-1]:
                continue
            if target >= row[0] and target <= row[-1]:
                for num in row:
                    if num == target:
                        return True
        return False
        