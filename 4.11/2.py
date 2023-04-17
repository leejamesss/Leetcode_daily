# https://leetcode.cn/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
#双指针
#快指针和慢指针遍历，只是对应的操作为删除操作

