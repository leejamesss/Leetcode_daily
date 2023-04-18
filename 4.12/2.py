# https://leetcode.cn/problems/divide-two-integers/
#位运算、二分查找
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        # 特判除数为0以及被除数等于INT_MIN的情况
        if not divisor or (dividend == MIN_INT and divisor == -1):
            return MAX_INT
        # 计算被除数和除数的绝对值
        a, b = abs(dividend), abs(divisor)
        # 计算二进制数的最高位
        shift = 0
        while a >= b << shift:
            shift += 1
        # 从最高位开始逐渐减少除数的值，并将相应的商累加到结果中
        res = 0
        for i in range(shift-1, -1, -1):
            if a >= b << i:
                res += 1 << i
                a -= b << i
        # 根据题目要求进行结果的截断以及符号的调整
        return res if (dividend > 0) == (divisor > 0) else -res
#除数左移，直到其大于被除数的一半
#确定二进制数的最高位
