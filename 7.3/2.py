class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == size-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
# https://leetcode.cn/problems/binary-tree-right-side-view/submissions/
