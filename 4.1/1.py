#https://leetcode.cn/problems/regular-expression-matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # 空字符串能够匹配空正则表达式
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    # * 匹配 0 个字符
                    dp[i][j] = dp[i][j-2]
                    # * 匹配至少一个字符
                    if i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

