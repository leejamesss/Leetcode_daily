class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        cnt = 0
        
        for i in range(2, n):
            if is_prime[i]:
                cnt += 1
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
        
        return cnt

# https://leetcode.cn/problems/count-primes/submissions/
