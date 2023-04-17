# https://leetcode.cn/problems/3sum/
#双指针
#排序
#将当前元素作为三元组中的第一个元素，将剩下的元素看作是一个二元组，在其中寻找和为当前元素的相反数的两个元素
#遍历数组时跳过相同的元素
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans
