# https://leetcode.cn/problems/gray-code/
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]  # 初始化为 [0]
        for i in range(n):
            add = 1 << i  # 计算需要在哪一位加 1
            for j in range(len(res)-1, -1, -1):
                # 从后往前遍历，并在每个数前加上 add
                res.append(res[j] + add)
        return res
