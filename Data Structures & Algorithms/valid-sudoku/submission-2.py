class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  

        for i in range(9):
            for j in range(9):
                entry = board[i][j]
                if entry == ".":
                    continue
                
                if entry in rows[i]:
                    return False
                else:
                    rows[i].add(entry)

                if entry in cols[j]:
                    return False
                else:
                    cols[j].add(entry)
                
                index = (i//3) * 3 + (j//3)
                if entry in boxes[index]:
                    return False
                else:
                    boxes[index].add(entry)
        return True
        """
        flag = True
        for row in board:
            row_set = set()
            for entry in row:
                if entry != ".":
                    if entry not in row_set:
                        row_set.add(entry)
                    else:
                        flag = False
                        return False
        for j in range(9):
            col_set = set()
            for i in range(9):
                entry = board[i][j]
                if entry != ".":
                    if entry not in col_set:
                        col_set.add(entry)
                    else:
                        flag = False
                        return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        entry = board[r][c]
                        if entry != ".":
                            if entry not in box_set:
                                box_set.add(entry)
                            else:
                                flag = False
                                return False
        return flag
        """
