

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = 0
        candidate1 = candidate2 = None
        n = len(nums)
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        if nums.count(candidate1) > n // 3:
            res.append(candidate1)
        if nums.count(candidate2) > n // 3:
            res.append(candidate2)
        return res
#  https://leetcode.cn/problems/majority-element-ii/submissions/
