# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/submissions/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # mid 在后半段有序区间内
                left = mid + 1
            else: # mid 在前半段有序区间内
                right = mid

        return nums[left]
