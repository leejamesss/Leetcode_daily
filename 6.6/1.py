# https://leetcode.cn/problems/palindrome-partitioning-ii/
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp 数组初始化为 0

        # 预处理 is_palindrome 数组，用于判断回文字符串
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True

        for i in range(1, n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i  # 最坏情况下，每个字符都需要分割一次
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
                        
        return dp[n-1]
