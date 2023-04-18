
# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
#滑动窗口思想
#  words 中的所有字符串长度相同，
# 将 s 分割成若干个长度为 m 的子串，并检查每个子串是否包含 words 中所有字符串
#哈希表记录 words 中所有字符串出现的次数
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        n, m, k = len(s), len(words[0]), len(words)
        if n < m * k:
            return []
        res = []
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        for i in range(m):
            left, right = i, i
            cur_dict = {}
            while right + m <= n:
                word = s[right:right+m]
                right += m
                if word not in word_dict:
                    left = right
                    cur_dict.clear()
                else:
                    if word not in cur_dict:
                        cur_dict[word] = 1
                    else:
                        cur_dict[word] += 1
                    while cur_dict[word] > word_dict[word]:
                        cur_dict[s[left:left+m]] -= 1
                        left += m
                    if right - left == k * m:
                        res.append(left)
        return res
