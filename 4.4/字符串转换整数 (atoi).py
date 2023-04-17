# 链接：https://leetcode.cn/problems/string-to-integer-atoi
#题目要实现一个字符串转换成整数的函数 
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()           #读入字符串并丢弃无用的前导空格
        if not s:               # 如果没有读入数字，则整数为 0 
            return 0
        sign = 1
        index = 0
        if s[index] == '+':     #检查下一个字符（假设还未到字符末尾）为正还是负号
            index += 1
        elif s[index] == '-':
            index += 1
            sign = -1
        result = 0
        while index < len(s) and s[index].isdigit():    #读入下一个字符，直到到达下一个非数字字符或到达输入的结尾
            result = result * 10 + int(s[index])        # 将前面步骤读入的这些数字转换为整数
            index += 1
            if result > 2 ** 31 - 1:                  
                break
        result *= sign
        # 如果整数数超过 32 位有符号整数范围 [−231, 231 − 1] ，需要截断这个整数，使其保持在这个范围内
        if result < -2 ** 31:
            result = -2 ** 31       #小于 −231 的整数应该被固定为 −231
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1    #大于 231 − 1 的整数应该被固定为 231 − 1
        return result
   


