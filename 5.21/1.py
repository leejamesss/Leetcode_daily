#https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)
        is_left_to_right = True  # 标识从左往右遍历

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if is_left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
            is_left_to_right = not is_left_to_right

        return res
