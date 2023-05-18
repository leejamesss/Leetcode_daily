# https://leetcode.cn/problems/additive-number/
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        def addStrings(s1, s2):
            res = ""
            i, j, carry = len(s1)-1, len(s2)-1, 0
            while i >= 0 or j >= 0 or carry > 0:
                curr = carry
                if i >= 0:
                    curr += ord(s1[i]) - ord('0')
                    i -= 1
                if j >= 0:
                    curr += ord(s2[j]) - ord('0')
                    j -= 1
                carry = curr // 10
                curr = curr % 10
                res = str(curr) + res
            return res
                
        def backtrack(num1, num2, start):
            if start == n:
                return True
            
            for i in range(start, n):
                # 当前数字以0开头，只能是0
                if num[start] == '0' and i > start:
                    break
                cur = addStrings(num1, num2)
                # 如果当前数字不等于前两个数字之和，则剪枝
                if not num[start:i+1] == cur:
                    continue
                # 找到了符合条件的数字，继续向下搜索
                if backtrack(num2, cur, i+1):
                    return True
                
            return False
        
        for i in range(1, n):
            # 第一个数字以0开头，只能是0
            if num[0] == '0' and i > 1:
                break
            num1 = num[:i]
            for j in range(i+1, n):
                # 第二个数字以0开头，只能是0
                if num[i] == '0' and j > i+1:
                    break
                num2 = num[i:j]
                if backtrack(num1, num2, j):
                    return True
                
        return False
