# https://leetcode.cn/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxpoint = 0
        n = len(nums)
        for i in range(n):
            if i > maxpoint: # 如果当前位置无法到达，则直接返回 False
                return False
            maxpoint = max(maxpoint, i + nums[i])
        return True
