# https://leetcode.cn/problems/n-queens-ii/
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 初始化列、对角线和反对角线的占用情况
        cols = set()
        diag1 = set()
        diag2 = set()
        # 初始化计数器
        count = 0
        
        def backtrack(row):
            nonlocal count
            # 如果已经放置了n个皇后，将计数器加1
            if row == n:
                count += 1
                return
            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                # 如果当前列、对角线或反对角线已经被占用，跳过该列
                if col in cols or row+col in diag1 or row-col in diag2:
                    continue
                # 放置皇后，并更新列、对角线和反对角线的占用情况
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                # 递归处理下一行
                backtrack(row+1)
                # 恢复原来的状态，继续尝试下一列
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
                
        backtrack(0)
        return count
