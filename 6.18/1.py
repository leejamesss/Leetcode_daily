# https://leetcode.cn/problems/maximum-gap/submissions/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        nums.sort()
        max_diff = 0
        for i in range(n - 1):
            max_diff = max(max_diff, nums[i + 1] - nums[i])
        return max_diff
