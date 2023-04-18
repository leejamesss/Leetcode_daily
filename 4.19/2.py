# https://leetcode.cn/problems/first-missing-positive/
#置换思想
#置换无效数字
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 特判数组为空和长度为 1 的情况
        if not nums:
            return 1
        if len(nums) == 1:
            return 1 if nums[0] <= 0 or nums[0] > 1 else 2

        # 将无效数字设为 -1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = -1

        # 进行置换操作
        for i in range(len(nums)):
            while nums[i] != -1 and nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        # 找到第一个没有出现的正整数
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        # 如果数组中所有数字都出现，则返回数组长度+1
        return len(nums) + 1
