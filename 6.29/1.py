# https://leetcode.cn/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)
        return nums
      
