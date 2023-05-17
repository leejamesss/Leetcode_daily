class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        # 回溯构造表达式
        def backtrack(expr, i, res, mul):
            if i == n:
                if res == target:
                    ans.append("".join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                # 占位符 + 数字
                expr.append("")
            val = 0
            for j in range(i, n):
                # 如果有前导零，那么这个数只能是0
                if j > i and num[i] == "0":
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:
                    backtrack(expr, j + 1, val, val)
                else:
                    expr[signIndex] = "+"; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = "-"; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = "*"; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans
# https://leetcode.cn/problems/expression-add-operators/submissions/
