
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]  # 初始化记忆化数组
        
        def dfs(i, j):
            if memo[i][j] > 0:  # 如果已经计算过路径长度，直接返回之前的结果
                return memo[i][j]
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            res = 1  # 如果四个方向都搜索不到递增路径，则默认路径长度为 1
            for di, dj in directions:  # 对于每一个方向
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    # 如果当前方向对应位置的数值严格大于当前位置的数值
                    # 沿着当前方向继续递归，得到从当前位置出发的最长递增路径长度
                    res = max(res, dfs(ni, nj) + 1)
            
            memo[i][j] = res  # 记录当前位置的最长递增路径长度
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))  # 枚举每个位置，计算所有位置中最长递增路径的长度
        return ans

# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/submissions/
