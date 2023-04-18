# https://leetcode.cn/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    # 如果当前位置无法填入任何数字，则说明前面填错了
                    return False
        return True
    
    def isValid(self, board, row, col, num):
        # 检查行中是否有重复数字
        for i in range(9):
            if board[row][i] == num:
                return False
        # 检查列中是否有重复数字
        for i in range(9):
            if board[i][col] == num:
                return False
        # 检查当前 3x3 宫中是否有重复数字
        x = (row // 3) * 3
        y = (col // 3) * 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] == num:
                    return False
        return True
