class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for i in range(len(pattern)):
            p, w = pattern[i], words[i]
            if p in p2w and p2w[p] != w or w in w2p and w2p[w] != p:
                return False
            p2w[p], w2p[w] = w, p
        return True
# https://leetcode.cn/problems/word-pattern/submissions/
