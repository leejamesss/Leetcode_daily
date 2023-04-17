#最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/

#思路：中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2

        return s[start:end+1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


