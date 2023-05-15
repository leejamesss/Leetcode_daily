class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:  # 当前节点为空，返回空节点
            return None
        # 交换左右子树
        root.left, root.right = root.right, root.left
        # 递归左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# https://leetcode.cn/problems/invert-binary-tree/submissions/
