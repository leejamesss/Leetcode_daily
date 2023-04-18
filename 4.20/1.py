
#https://leetcode.cn/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        stack = []  # 栈中存储的是柱子的下标
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur_pos = stack.pop()  # 弹出栈顶元素
                if not stack:
                    break
                left_pos = stack[-1]  # 左边界
                width = i - left_pos - 1  # 计算能够存储雨水的宽度
                height_diff = min(height[left_pos], height[i]) - height[cur_pos]  # 计算能够存储雨水的高度
                ans += width * height_diff
            stack.append(i)
        
        return ans
#首先考虑两个柱子
#推广到多个柱子
