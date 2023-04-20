# https://leetcode.cn/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])
        
        # 初始化 dp 数组
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # 处理第一行和第一列的 dp 值
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 计算其余位置的 dp 值
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
