# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            n = len(nums)
            if n <= 2:
                return n
            
            slow, fast = 2, 2
            while fast < n:
                if nums[fast] != nums[slow-2]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1
            
            return slow
# 快慢          
  
