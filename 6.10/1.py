
# https://leetcode.cn/problems/word-break-ii/submissions/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        # 使用哈希表保存每个单词
        word_set = set(wordDict)
        # 动态规划求解 s 是否能被拆分为 wordDict 中的单词
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
        # 回溯算法构造所有可行的划分方案
        res = []
        path = []
        self.dfs(s, word_set, dp, 0, path, res)
        return res

    def dfs(self, s, word_set, dp, start, path, res):
        if start == len(s):
            res.append(' '.join(path))
            return
        for end in range(start + 1, len(s) + 1):
            if dp[end] and s[start:end] in word_set:
                path.append(s[start:end])
                self.dfs(s, word_set, dp, end, path, res)
                path.pop()
