class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []  # 结果列表

        def backtrack(cur_sum, k, n, start, path, res):
            if cur_sum == n and k == 0:  # 如果当前已经选中的数的和等于目标和n并且已经选择了k个数，则将当前path加入res
                res.append(path[:])  # 注意要用path[:]复制一份，否则可能引起错误
            for i in range(start, 10):
                if i > n - cur_sum:  # 如果i已经大于n-cur_sum，则后续数字加上i也一定会大于n，因此直接退出循环
                    break
                if i in path:  # 如果数字i已经在path中，则跳过该数字
                    continue
                path.append(i)  # 将数字i加入path中
                backtrack(cur_sum + i, k - 1, n, i + 1, path, res)  # 递归回溯
                path.pop()  # 回溯一步，将数字i从path中删除

        backtrack(0, k, n, 1, [], res)  # 开始回溯
        return res
# https://leetcode.cn/problems/combination-sum-iii/submissions/
