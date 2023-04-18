# https://leetcode.cn/problems/valid-sudoku/
#哈希表
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])
                    box_idx = (i // 3) * 3 + j // 3
                    if board[i][j] in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(board[i][j])
        return True
# 如果当前位置不是空白格，则检查它是否在对应的哈希表中已经存在
# 如果不存在，则将其加入哈希表中。
# 如果已经存在，则说明数独无效，返回 False
