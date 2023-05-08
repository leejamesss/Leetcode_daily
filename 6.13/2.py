
# https://leetcode.cn/problems/max-points-on-a-line/submissions/
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        # 每个点和它后面的点构成的线段所包含的点数
        table = defaultdict(lambda: defaultdict(int))
        res = 0
        for i in range(len(points)):
            same_points = 1 # 记录和点i坐标相同的点的数量（包括点i本身）
            for j in range(i+1, len(points)):
                dx, dy = points[j][0]-points[i][0], points[j][1]-points[i][1]
                if dx == dy == 0: # 重复的点
                    same_points += 1
                else:
                    gcd = self.compute_gcd(dx, dy) # 求dx和dy的最大公约数
                    dx, dy = dx//gcd, dy//gcd # 约分
                    table[(dx, dy)][i] += 1 # 更新包含点i的线段的点数
                    table[(dx, dy)][j] += 1 # 更新包含点j的线段的点数
            # 找出哈希表中最大的值
            if table:
                max_count = max([max(table[key].values()) for key in table])
            else:
                max_count = 0
            # 更新结果
            res = max(res, same_points+max_count)
            # 清空哈希表
            table.clear()
        return res
    
    # 辗转相减法求最大公约数
    def compute_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
