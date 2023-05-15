class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot = nums[r]
            i = l - 1
            for j in range(l, r):
                if nums[j] >= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[r] = nums[r], nums[i+1]
            return i + 1
        
        n = len(nums)
        l, r = 0, n - 1
        while True:
            pos = partition(l, r)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                r = pos - 1
            else:
                l = pos + 1
# https://leetcode.cn/problems/kth-largest-element-in-an-array/submissions/
