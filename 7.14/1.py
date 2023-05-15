class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1 - ax2) * abs(ay1 - ay2) # 计算第一个矩形的面积
        area2 = abs(bx1 - bx2) * abs(by1 - by2) # 计算第二个矩形的面积

        overlap_width = min(ax2, bx2) - max(ax1, bx1) # 重叠部分的宽度
        overlap_height = min(ay2, by2) - max(ay1, by1) # 重叠部分的高度
        overlap_area = max(overlap_width, 0) * max(overlap_height, 0) # 计算重叠部分的面积

        return area1 + area2 - overlap_area
# https://leetcode.cn/problems/rectangle-area/submissions/
