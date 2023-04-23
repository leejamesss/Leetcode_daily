# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        if n == 0:
            return False

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]: # 左半边是有序的
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # 右半边是有序的
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
