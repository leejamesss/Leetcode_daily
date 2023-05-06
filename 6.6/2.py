# https://leetcode.cn/problems/clone-graph/

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # 如果这个节点已经被访问过，则直接返回对应的拷贝
        if node in self.visited:
            return self.visited[node]

        # 新建一个节点作为拷贝
        clone_node = Node(node.val, [])

        # 将新节点添加到 visited 哈希表中
        self.visited[node] = clone_node

        # 遍历 node 的邻居，并递归调用 cloneGraph() 方法
        for neighbor in node.neighbors:
            clone_neighbor = self.cloneGraph(neighbor)
            clone_node.neighbors.append(clone_neighbor)

        return clone_node
