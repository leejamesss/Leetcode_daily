
# https://leetcode.cn/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, target, path):
            # 如果目标整数等于0，则说明已经找到了一组解
            if target == 0:
                res.append(path)
                return
            # 从当前位置开始遍历 candidates 数组
            for i in range(index, len(candidates)):
                # 如果当前数字大于目标整数，退出循环
                if candidates[i] > target:
                    break
                # 防止重复组合
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                # 选择当前数字，继续递归搜索
                backtrack(i+1, target - candidates[i], path + [candidates[i]])
        res = []
        candidates.sort()
        backtrack(0, target, [])
        return res
#回溯递归
