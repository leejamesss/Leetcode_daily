# https://leetcode.cn/problems/excel-sheet-column-number/submissions/
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = res * 26 + ord(c) - ord('A') + 1
        return res
