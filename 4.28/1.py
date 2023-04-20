#https://leetcode.cn/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            # 如果到达终点，则返回 1
            if x == m-1 and y == n-1:
                return 1

            # 如果已经计算过当前位置，则直接返回计算结果
            if memo[x][y] != -1:
                return memo[x][y]

            # 向右移动
            right = 0
            if y+1 < n:
                right = dfs(x, y+1)

            # 向下移动
            down = 0
            if x+1 < m:
                down = dfs(x+1, y)

            # 计算到达 (x,y) 的总路径数，并保存到 memo 数组中
            memo[x][y] = right + down
            return memo[x][y]

        return dfs(0, 0)

# 测试代码
if __name__ == '__main__':
    sol = Solution()
    # Testcase 1
    m1 = 3
    n1 = 7
    res1 = sol.uniquePaths(m1, n1)
    print(res1)  # expected output: 28

    # Testcase 2
    m2 = 3
    n2 = 2
    res2 = sol.uniquePaths(m2, n2)
    print(res2)  # expected output: 3

    # Testcase 3
    m3 = 7
    n3 = 3
    res3 = sol.uniquePaths(m3, n3)
    print(res3)  # expected output: 28

    # Testcase 4
    m4 = 3
    n4 = 3
    res4 = sol.uniquePaths(m4, n4)
    print(res4)  # expected output: 6
