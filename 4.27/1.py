# https://leetcode.cn/problems/spiral-matrix/submissions/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
            #去头
            res+=matrix.pop(0)
            #旋转90度
            matrix=list(zip(*matrix))[::-1]
        return res
 #关键在于移动的相对性，移动矩阵即可

#补充知识点：矩阵的旋转
#Zip实现矩阵旋转

#方法1：直接调用numpy
#方法2：zip直接转换
