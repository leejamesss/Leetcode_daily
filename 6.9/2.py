# https://leetcode.cn/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break
        return dp[-1]
