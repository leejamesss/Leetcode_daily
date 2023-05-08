# https://leetcode.cn/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # dp[i][0] 表示以 nums[i] 结尾的子数组的最大乘积
        # dp[i][1] 表示以 nums[i] 结尾的子数组的最小乘积
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        res = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                dp[i][0] = max(dp[i-1][0] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i][0] = max(dp[i-1][1] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][0] * nums[i], nums[i])
            res = max(res, dp[i][0])

        return res
