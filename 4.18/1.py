
# https://leetcode.cn/problems/count-and-say/

#递归
#手动找规律

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        pre = self.countAndSay(n - 1)
        res = ""
        i = 0
        while i < len(pre):
            j = i + 1
            while j < len(pre) and pre[j] == pre[i]:
                j += 1
            res += str(j - i) + pre[i]
            i = j
        return res
