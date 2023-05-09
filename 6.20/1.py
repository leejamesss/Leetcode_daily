# https://leetcode.cn/problems/excel-sheet-column-title/submissions/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            num = (columnNumber - 1) % 26  # 求最后一位字符的编号
            result.append(chr(ord('A') + num))  # 将编号转为字母并添加到结果列表中
            columnNumber = (columnNumber - 1) // 26  # 更新 columnNumber
        return ''.join(result[::-1])  # 将结果列表翻转并拼接成字符串
