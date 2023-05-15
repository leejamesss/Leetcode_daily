class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # dp[i] 表示前 i 家房屋所能抢到的最大金额
        # 不偷窃最后一家，范围为 nums[:n-1]
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        ans1 = dp[n-1]
        # 不偷窃第一家，范围为 nums[1:]
        dp = [0] * (n+1)
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        ans2 = dp[n-1]
        return max(ans1, ans2)
#       https://leetcode.cn/problems/house-robber-ii/submissions/
