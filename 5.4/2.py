# https://leetcode.cn/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0, col0 = False, False
        
        # 检查第一行和第一列
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break
        
        # 扫描整个矩阵，并使用第一行和第一列作为标记数组
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # 根据第一行和第一列的标记，将对应的行和列全部置为 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 处理第一行和第一列
        if row0:
            matrix[0] = [0] * n
        if col0:
            for i in range(m):
                matrix[i][0] = 0
