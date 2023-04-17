
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
#双指针问题，快指针和慢指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                      #边界条件处理
            return 0    
        n = len(nums)                     
        slow = 0                          #慢指针
        for fast in range(1, n):          #快指针（遍历）
            if nums[fast] != nums[slow]:  
                slow += 1                 
                nums[slow] = nums[fast]   #如果不相等，就让慢指针等于快指针的数，效果是把不重复的数字移动到lst的前部
        return slow + 1
#实质上，slow+1承载了两个信息：
#1、慢指针的位置信息
#2、不重复的元素个数
