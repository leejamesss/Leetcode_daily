# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        max_profit = 0
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit
