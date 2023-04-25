#https://leetcode.cn/problems/binary-tree-level-order-traversal/
#BFS
#队列

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            level_size = len(queue)  # 当前层的节点数

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res
