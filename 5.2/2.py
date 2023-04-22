# https://leetcode.cn/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev1, prev2 = 1, 2
        for i in range(3, n + 1):
            cur = prev1 + prev2
            prev1, prev2 = prev2, cur
        return cur
