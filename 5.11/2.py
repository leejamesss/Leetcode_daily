#https://leetcode.cn/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [-1] # 用-1表示左边界
        max_area = 0
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                max_area = max(max_area, (i - stack[-1] - 1) * heights[top])
            stack.append(i)
        while stack[-1] != -1:
            top = stack.pop()
            max_area = max(max_area, (n - stack[-1] - 1) * heights[top])
        return max_area
