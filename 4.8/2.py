# https://leetcode.cn/problems/generate-parentheses/
#回溯算法
#穷举

#left 和 right 分别表示已经添加的左括号和右括号的数量
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:          
                backtrack(s + '(', left + 1, right)
            if right < left:                    
                backtrack(s + ')', left, right + 1)
        backtrack('', 0, 0)
        return res
