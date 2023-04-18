# https://leetcode.cn/problems/multiply-strings/
#模拟列竖式运算
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i+j, i+j+1
                total_sum = mul + result[p2]
                
                result[p1] += total_sum // 10
                result[p2] = total_sum % 10
        
        # 去除前导零
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        
        return ''.join(map(str, result[i:]))
