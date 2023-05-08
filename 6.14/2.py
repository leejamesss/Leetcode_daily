# https://leetcode.cn/problems/reverse-words-in-a-string/submissions/
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 去掉前导空格和尾随空格
        n = len(s)
        if n == 0:
            return ""
        s = list(s)

        # 反转整个字符串
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        # 反转每个单词
        l, r = 0, 0
        while r < n:
            # 找到一个单词的区间 [l, r]
            while r < n and s[r] != ' ':
                r += 1
            # 翻转这个单词
            start, end = l, r - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            # 跳过单词间的空格
            while r < n and s[r] == ' ':
                r += 1
            l = r

        # 将多个空格变为一个空格
        i = 0
        for j in range(n):
            if s[j] != ' ' or (j > 0 and s[j-1] != ' '):
                s[i] = s[j]
                i += 1
        return "".join(s[:i])
