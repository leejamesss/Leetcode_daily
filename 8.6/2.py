

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        res = [0] * n
        mid = (n - 1) // 2
        i, j = mid, n - 1
        for k in range(n):
            if k % 2 == 0:
                res[k] = nums[i]
                i -= 1
            else:
                res[k] = nums[j]
                j -= 1
        nums[:] = res[:]

# https://leetcode.cn/problems/wiggle-sort-ii/submissions/
