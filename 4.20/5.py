#https://leetcode.cn/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化矩阵
        matrix = [[0]*n for _ in range(n)]

        # 定义四个方向
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0

        # 初始化位置和当前数值
        row, col = 0, 0
        num = 1

        while num <= n*n:
            matrix[row][col] = num
            num += 1

            # 计算下一个位置
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]

            # 判断是否需要更换方向
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or matrix[next_row][next_col] != 0:
                direction_index = (direction_index + 1) % 4

            # 更新位置
            row += directions[direction_index][0]
            col += directions[direction_index][1]

        return matrix
