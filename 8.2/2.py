class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # 添加两侧的虚拟气球，避免边界问题
        nums.insert(0, 1)
        nums.append(1)
        # 初始化 dp 数组
        dp = [[0] * (n+2) for _ in range(n+2)]
        # 动态转移
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])
        return dp[1][n]
#       https://leetcode.cn/problems/burst-balloons/submissions/
