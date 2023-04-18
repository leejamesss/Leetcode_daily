
# https://leetcode.cn/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # 栈底加入-1，代表栈底位置
        res = 0 # 初始化结果
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # 如果栈为空，说明前面的字符已经全部匹配完了，当前字符没有匹配，所以要把它压进栈里，代表直到这个位置，前面所有的字符都是有效括号
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])#计算当前右括号与其匹配左括号之间的长度：更新答案为当前答案与 i 减去栈顶元素后的值中的较大值
        return res
