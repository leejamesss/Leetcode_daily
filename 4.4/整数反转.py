# https://leetcode.cn/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:
        max_int, min_int = 2**31-1, -2**31
        
        res = 0
        is_negative = x < 0                     #记录输入数字的符号
        x = abs(x)
        while x != 0:                           #输入数字转为正数进行反转操作        
            if res > max_int // 10 or (res == max_int // 10 and x % 10 > 7):
                return 0
            if res < min_int // 10 or (res == min_int // 10 and x % 10 < -8):
                return 0
            res = res * 10 + x % 10
            x //= 10
        
        if is_negative:                         #决定是否加上负号
            res = -res
            
        return res
    

