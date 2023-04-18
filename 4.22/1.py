# https://leetcode.cn/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def backtrack(first):
            nonlocal ans
            
            if first == n:
                ans.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack(0)
        return ans
#回溯算法
  
