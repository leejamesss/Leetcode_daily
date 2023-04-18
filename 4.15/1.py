
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

#二分查找 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left, right = 0, n - 1
        # 二分查找目标值的起始位置
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        start = left
        # 二分查找目标值的结束位置
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        end = right
        return [start, end]
