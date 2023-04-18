# https://leetcode.cn/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = abs(n)
        sub = self.myPow(x, n // 2)
        if n % 2 == 0:
            return sub * sub
        else:
            return sub * sub * x
