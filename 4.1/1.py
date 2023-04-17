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

#dp[i][j] 表示 s 的前 i 个字符和 p 的前 j 个字符是否匹配
#如果 p[j] 是小写字母或者 '.'，则 dp[i][j] 只有在 dp[i-1][j-1] 为 true 且 s[i] 和 p[j] 匹配的情况下才为 true
#如果 p[j] 是 '*'，则有两种情况：
#   如果 * 匹配 0 个字符，则 dp[i][j] 取决于 dp[i][j-2]
#   如果 * 匹配至少一个字符，则 dp[i][j] 取决于 dp[i-1][j] 和 dp[i][j-1] 是否为 true
#边界情况：dp[0][0] = true，表示空字符串能够匹配空正则表达式
#时间复杂度是 O(mn),空间复杂度也是O(mn),分别是p和s的长度
