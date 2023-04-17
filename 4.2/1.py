# https://leetcode.cn/problems/container-with-most-water
#双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化左右指针及最大面积
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # 计算当前面积
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            # 移动指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

