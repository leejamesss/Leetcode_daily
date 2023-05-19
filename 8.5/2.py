

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMax(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(num1, num2):
            res = []
            while num1 or num2:
                if num1 >= num2:
                    res.append(num1[0])
                    num1 = num1[1:]
                else:
                    res.append(num2[0])
                    num2 = num2[1:]
            return res
            
        ans = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                max1 = getMax(nums1, i)
                max2 = getMax(nums2, k - i)
                max_num = merge(max1, max2)
                ans = max(ans, max_num)
        return ans

# https://leetcode.cn/problems/create-maximum-number/submissions/
