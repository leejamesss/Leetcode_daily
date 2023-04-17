#https://leetcode.cn/problems/zigzag-conversion/
#N字型变换
#思路：使用模拟的方式来解决
#list来存储每一行的字符
#遍历输入字符串，根据当前字符所在的行数，在对应的行末尾添加该字符。
#当行数达到 numRows 或者为 1 时，行数应该反转。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                #当 numRows 为 1 时，直接返回原字符串
            return s

        rows = [''] * numRows           #初始时每个元素均为空串，表示每一行还没有任何字符
        cur_row = 0                     #cur_row 表示当前行数
        going_down = False              #going_down 表示当前行是否处于向下方向

        for c in s:                     #遍历输入字符串，对于每个字符 c，将其添加到对应的行末尾
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:    #当 cur_row 达到边界时，行数需要反转
                going_down = not going_down           
            cur_row += 1 if going_down else -1            
        
        return ''.join(rows)                              #将每一行的字符拼接起来得到最终结果
