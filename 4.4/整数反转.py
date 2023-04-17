class Solution:
    def reverse(self, x: int) -> int:
        max_int, min_int = 2**31-1, -2**31
        
        res = 0
        is_negative = x < 0
        x = abs(x)
        while x != 0:
            if res > max_int // 10 or (res == max_int // 10 and x % 10 > 7):
                return 0
            if res < min_int // 10 or (res == min_int // 10 and x % 10 < -8):
                return 0
            res = res * 10 + x % 10
            x //= 10
        
        if is_negative:
            res = -res
            
        return res
