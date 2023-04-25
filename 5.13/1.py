# https://leetcode.cn/problems/scramble-string/submissions/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        if s1 == s2:
            return True
        # 判断字符是否相同
        if sorted(s1) != sorted(s2):
            return False
        
        # 创建三维数组 dp
        # dp[i][j][k] 表示 s1 从 i 开始，s2 从 j 开始，长度为 k 的子字符串是否可以通过扰乱得到。
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        
        # 初始化单个字符的情况
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        
        # 枚举子字符串的长度
        for k in range(2, n+1):
            # 枚举 s1 中的起始位置
            for i in range(n-k+1):
                # 枚举 s2 中的起始位置
                for j in range(n-k+1):
                    # 枚举分割的位置
                    for p in range(1, k):
                        # 不交换的情况
                        if dp[i][j][p] and dp[i+p][j+p][k-p]:
                            dp[i][j][k] = True
                            break
                        # 交换的情况
                        if dp[i][j+k-p][p] and dp[i+p][j][k-p]:
                            dp[i][j][k] = True
                            break
        
        return dp[0][0][n]
