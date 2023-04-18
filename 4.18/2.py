# https://leetcode.cn/problems/combination-sum/
#回溯算法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index: int, target: int, path: List[int]):
            if target == 0:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
        res = []
        # 首先将数组从小到大排序
        candidates.sort()
        backtrack(0, target, [])
        return res
