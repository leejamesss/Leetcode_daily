class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # 将 res 左移一位，腾出最低位的位置
            res <<= 1
            # 获取 n 的最低位并加到 res 中
            res |= n & 1
            # 将 n 右移一位，去掉已经处理过的最低位
            n >>= 1
        return res
# https://leetcode.cn/problems/reverse-bits/solution/
