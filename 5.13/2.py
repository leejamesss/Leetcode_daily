# https://leetcode.cn/problems/merge-sorted-array/submissions/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        # 双指针，从后向前比较
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

        nums1[:p2+1] = nums2[:p2+1]
