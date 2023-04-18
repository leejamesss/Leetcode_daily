# https://leetcode.cn/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化列、对角线和反对角线的占用情况
        cols = set()                              
        diag1 = set()
        diag2 = set()
        # 初始化棋盘
        board = [['.'] * n for _ in range(n)]
        # 初始化结果集
        res = []
        
        def backtrack(row):
            # 如果已经放置了n个皇后，将当前解添加到结果集中
            if row == n:
                res.append([''.join(row) for row in board])
                return
            # 尝试在当前行的每一列放置皇后
            for col in range(n):                                  
                # 如果当前列、对角线或反对角线已经被占用，跳过该列
                if col in cols or row+col in diag1 or row-col in diag2:
                    continue
                # 放置皇后，并更新列、对角线和反对角线的占用情况
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                # 递归处理下一行
                backtrack(row+1)
                # 恢复原来的状态，继续尝试下一列
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
                
        backtrack(0)
        return res
#回溯算法
#枚举+剪枝
  
