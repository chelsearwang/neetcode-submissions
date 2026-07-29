class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0]) * len(matrix) - 1
        cols = len(matrix[0])
        while left <= right:
            middle = (left+right)//2
            r = middle // cols
            c = middle % cols
            print(middle, r, c)
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                right = middle - 1
            else:
                left = middle + 1
        return False
        """
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[-1]:
                continue
            if target >= row[0] and target <= row[-1]:
                left = 0
                right = len(row) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if row[middle] == target:
                        return True
                    elif row[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
                return False
        return False
        """