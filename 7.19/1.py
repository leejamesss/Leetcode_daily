# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        # 如果当前节点的值比 p 和 q 都大，则递归左子树
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # 如果当前节点的值比 p 和 q 都小，则递归右子树
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # 否则，当前节点就是它们的最近公共祖先
        else:
            return root
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
