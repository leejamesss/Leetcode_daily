# https://leetcode.cn/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        lst=[]
        for i in digits:
            num+=str(i)
        num=str(int(num)+1)
        for s in num:
            lst.append(int(s))
        return lst
