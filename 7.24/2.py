# https://leetcode.cn/problems/ugly-number-ii/



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i_2, i_3, i_5 = 0, 0, 0
        for i in range(1, n):
            ugly = min(nums[i_2] * 2, nums[i_3] * 3, nums[i_5] * 5)
            nums.append(ugly)
            if nums[i_2] * 2 == ugly:
                i_2 += 1
            if nums[i_3] * 3 == ugly:
                i_3 += 1
            if nums[i_5] * 5 == ugly:
                i_5 += 1
        return nums[n - 1]
