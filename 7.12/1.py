class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i
        return False
# https://leetcode.cn/problems/contains-duplicate-ii/submissions/
