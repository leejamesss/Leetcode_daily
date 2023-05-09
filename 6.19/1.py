#https://leetcode.cn/problems/fraction-to-recurring-decimal/submissions/
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        # 判断结果的符号，并将分子和分母都转换为正数进行运算
        if numerator * denominator < 0:
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        # 先计算整数部分
        result = numerator // denominator
        res.append(str(result))
        remainder = numerator % denominator
        # 如果有余数，则需要计算小数部分
        if remainder != 0:
            res.append(".")
            # 用字典记录每个余数出现的位置，方便后面加括号
            remainder_index = {}
            while remainder != 0:
                # 如果有循环小数，则加上括号
                if remainder in remainder_index:
                    res.insert(remainder_index[remainder], "(")
                    res.append(")")
                    break
                remainder_index[remainder] = len(res)
                remainder *= 10
                res.append(str(remainder // denominator))
                remainder %= denominator
        return "".join(res)
