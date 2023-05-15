class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        bucket = {}
        for i in range(n):
            # 计算当前元素所在的桶编号
            idx = nums[i] // (t+1)
            if idx in bucket:
                return True
            if idx-1 in bucket and abs(nums[i]-bucket[idx-1]) <= t:
                return True
            if idx+1 in bucket and abs(nums[i]-bucket[idx+1]) <= t:
                return True
            bucket[idx] = nums[i]
            # 删除下标范围不符合要求的桶
            if i >= k:
                del_idx = nums[i-k] // (t+1)
                del bucket[del_idx]
        return False
# https://leetcode.cn/problems/contains-duplicate-iii/submissions/
