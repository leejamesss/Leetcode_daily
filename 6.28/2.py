class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if k > n//2:
            # 如果k达到了极大值，则相当于不限制交易次数，使用第二题的做法
            dp_0, dp_1 = 0, -prices[0]
            for i in range(1, n):
                tmp = dp_0
                dp_0 = max(dp_0, dp_1+prices[i])
                dp_1 = max(dp_1, tmp-prices[i])
            return dp_0

        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        return dp[n-1][k][0]
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/submissions/
