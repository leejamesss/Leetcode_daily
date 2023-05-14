class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        res = float("inf")
        sum = 0
        
        while right < n:
            sum += nums[right]
            
            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
            
            right += 1
        
        if res == float("inf"):
            return 0
        else:
            return res
# https://leetcode.cn/problems/minimum-size-subarray-sum/submissions/
