# https://leetcode.cn/problems/maximal-rectangle/submissions/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = [-1] # 用-1表示左边界
            for i in range(n):
                while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    max_area = max(max_area, (i - stack[-1] - 1) * heights[top])
                stack.append(i)
            while stack[-1] != -1:
                top = stack.pop()
                max_area = max(max_area, (n - stack[-1] - 1) * heights[top])
        return max_area
