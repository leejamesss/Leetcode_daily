# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: # 如果当前节点为 null，则返回 0
            return 0
        leftDepth = self.maxDepth(root.left) # 递归求出左子树深度
        rightDepth = self.maxDepth(root.right) # 递归求出右子树深度
        return max(leftDepth, rightDepth) + 1 # 返回左右子树深度的较大值加一
