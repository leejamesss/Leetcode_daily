class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 先求出左子树和右子树的高度
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == right_depth:  # 左子树为满二叉树
            return (1 << left_depth) + self.countNodes(root.right)
        else:  # 右子树为满二叉树
            return (1 << right_depth) + self.countNodes(root.left)

    def getDepth(self, root: TreeNode) -> int:
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth
# https://leetcode.cn/problems/count-complete-tree-nodes/submissions/
