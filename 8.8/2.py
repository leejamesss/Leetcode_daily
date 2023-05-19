

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1  # 初始化当前缺失的最小正整数
        ans = 0  # 初始化需要添加数字的数量
        i = 0  # 初始化 nums 的指针
        
        while miss <= n:  # 只要还存在缺失的正整数
            if i < len(nums) and nums[i] <= miss:  # 如果 nums 中还有数，并且能够用当前的数字将 [1, nums[i]] 区间内的所有数字都表示出来
                miss += nums[i]  # 更新 miss 的值
                i += 1  # 移动指针
            else:  # 如果不能用当前的数字将 [1, nums[i]] 区间内的某个数表示出来
                miss += miss  # 添加数字 miss，更新 miss 的值
                ans += 1  # 记录需要添加的数字的数量
                
        return ans

# https://leetcode.cn/problems/patching-array/submissions/
