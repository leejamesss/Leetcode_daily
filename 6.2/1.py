# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for j in range(1, 3):
                if i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[n-1][2][0]
