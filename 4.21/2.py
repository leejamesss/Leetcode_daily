#贪心算法
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_idx, last_idx, jump = 0, 0, 0
        
        for i in range(n-1):
            max_idx = max(max_idx, i + nums[i])
            if i == last_idx:
                last_idx = max_idx
                jump += 1
        
        return jump
#从前往后遍历数组，找到最大的 
##思路：
# 选择下一步跳到最远的位置
# 更新 max_idx 和 last_idx
# 如果到达了 last_idx，则需要再跳一步
# 将跳数 jump 加 1
