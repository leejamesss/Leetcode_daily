class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # 存储连边信息
        adj = [set() for i in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        # 记录当前叶节点
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        # BFS 逐层剥洋葱
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                # 删除这条边
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
#       https://leetcode.cn/problems/minimum-height-trees/submissions/
