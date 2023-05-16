class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        lst=[]
        for i in range(33):
            tmp=2**i
            lst.append(tmp)
        return n in lst
#       https://leetcode.cn/problems/power-of-two/submissions/
