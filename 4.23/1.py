# https://leetcode.cn/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # 转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 翻转每一行
        for i in range(n):
            left, right = 0, n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
#沿着对角线进行翻转
# 再沿着中心竖直线交换每一行
