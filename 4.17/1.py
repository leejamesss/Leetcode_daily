#最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/

#思路：中心扩散
#从每个位置出发，向两边扩展，寻找以该位置为中心的最长回文子串。
#枚举每个位置作为回文串的中心，然后尝试向左右扩展，直到不能扩展为止
#由于回文串的长度可能为偶数，因此我们需要同时从当前位置和当前位置的下一个位置出发，分别进行扩展，并记录最长的回文子串。由于字符串长度为 n，共有 2n-1 个中心，所以总时间复杂度为 O(n^2)。
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
#首先判断字符串是否小于2，是就直接返回
#从每个位置出发向两边扩散，寻找以该位置为中心的最长回文子串，并记录下左右端点。最后返回找到的最长回文子串。

