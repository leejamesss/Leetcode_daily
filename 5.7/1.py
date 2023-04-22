# https://leetcode.cn/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(start):
            ans.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return ans
