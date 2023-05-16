class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += num % 10
                num //= 10
            num = tmp
        return num
# https://leetcode.cn/problems/add-digits/submissions/
