class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:  # 处理特殊情况
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # 初始化 dp 数组
        ans = 0  # 记录最大正方形的面积
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # 边界情况
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ans = max(ans, dp[i][j])  # 更新最大正方形的面积
        return ans ** 2
# https://leetcode.cn/problems/maximal-square/submissions/
