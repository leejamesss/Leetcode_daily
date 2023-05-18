# https://leetcode.cn/problems/super-ugly-number/


import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        p = [1] * m
        
        heap = [(primes[i] * dp[p[i]], i) for i in range(m)]
        heapq.heapify(heap)
        
        for i in range(2, n + 1):
            dp[i], idx = heap[0][0], heap[0][1]
            while heap and heap[0][0] == dp[i]:
                num, idx = heapq.heappop(heap)
                p[idx] += 1
                heapq.heappush(heap, (primes[idx] * dp[p[idx]], idx))
            
        return dp[n]
