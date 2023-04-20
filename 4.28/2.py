#https://leetcode.cn/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 获取障碍物网格的行数和列数
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 特判：如果起点或终点上有障碍物，则无法到达终点
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # 初始化 dp 数组
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # 处理第一行和第一列的障碍物
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # 计算 dp 数组
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]
