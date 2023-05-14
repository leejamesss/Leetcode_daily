# https://leetcode.cn/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        res = 0
        
        def dfs(x, y):
            visited[x][y] = True
            
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1':
                    dfs(nx, ny)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    dfs(i, j)
        
        return res
