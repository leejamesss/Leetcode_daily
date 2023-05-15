


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n == 0:
            return res
        left = nums[0]
        right = nums[0]
        for i in range(1, n):
            if nums[i] == right + 1:
                right = nums[i]
            else:
                res.append(str(left) + "->" + str(right) if left != right else str(left))
                left = nums[i]
                right = nums[i]
        res.append(str(left) + "->" + str(right) if left != right else str(left))
        return res


# https://leetcode.cn/problems/summary-ranges/submissions/
