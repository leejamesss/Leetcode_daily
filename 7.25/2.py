class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n+1)  # 初始化计数器
        
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
                
        i, s = n, count[n]
        while i > s:  # 寻找满足条件的最大h指数
            i -= 1
            s += count[i]
            
        return i
# https://leetcode.cn/problems/h-index/submissions/
