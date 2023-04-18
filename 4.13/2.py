# https://leetcode.cn/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            nums.reverse()
        else:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
#从右往左找到第一个不符合递增顺序的位置 i
#看成倒序的起点
#从右往左找到第一个大于 nums[i] 的位置 j
#交换 nums[i] 和 nums[j]
#最后再将 i 后面的数字按升序排列
