# https://leetcode.cn/problems/valid-number/
#DFA思路实现
class Solution:
    def isNumber(self, s: str) -> bool:
        # 状态集合
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4}, # 0. 起始的空格
            {'d': 2, '.': 4}, # 1. 小数点前的数字
            {'d': 2, '.': 3, 'e': 5, ' ': 8}, # 2. 小数点、小数点后的数字或者指数
            {'d': 3, 'e': 5, ' ': 8}, # 3. 当小数点前为空格时，小数点、小数点后的数字或者指数
            {'d': 3}, # 4. 小数点后的数字
            {'s': 6, 'd': 7}, # 5. 指数
            {'d': 7}, # 6. 指数符号后面的数字
            {'d': 7, ' ': 8}, # 7. 指数符号后面的数字（可以有空格）
            {' ': 8} # 8. 结尾的空格
        ]
        # 转移状态函数
        def get_col(c):
            if c.isdigit():
                return 'd'
            elif c in "+-":
                return 's'
            elif c in "eE":
                return 'e'
            elif c in ". ":
                return c
            else:
                return '?'
        # 初始状态为0
        state = 0
        for char in s:
            col = get_col(char)
            if col not in states[state]:
                return False
            state = states[state][col]
        # 如果最终状态是1，2，5之一，则表示是有效数字
        return state in [2, 3, 7, 8]
