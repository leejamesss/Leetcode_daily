# https://leetcode.cn/problems/subsets-ii/submissions/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    # 跳过重复元素
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(i + 1, path)
                used[i] = False
                path.pop()

        n = len(nums)
        nums.sort()
        res = []
        used = [False] * n
        backtrack(0, [])
        return res
