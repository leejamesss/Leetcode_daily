class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 计算左侧乘积
        left_product = [1] * n
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        # 计算右侧乘积，同时计算答案
        right_product = 1
        for i in range(n-1, -1, -1):
            left_product[i] *= right_product
            right_product *= nums[i]
        return left_product

# https://leetcode.cn/problems/product-of-array-except-self/submissions/
