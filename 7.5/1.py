# https://leetcode.cn/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_square_sum(n: int) -> int:
            ss = 0
            while n > 0:
                n, mod = divmod(n, 10)
                ss += mod ** 2
            return ss
        
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = get_square_sum(n)
        
        return n == 1
