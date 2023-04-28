# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 构建邻接表
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, 1))  # 正向边
            adj[b].append((a, 0))  # 反向边

        # 递归访问城市并标记需要变更方向的边
        def dfs(node):
            nonlocal ans
            for nxt, direction in adj[node]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                if direction == 1:  # 需要变更方向的边
                    ans += 1
                dfs(nxt)

        ans = 0
        visited = [False] * n
        visited[0] = True
        dfs(0)
        return ans
