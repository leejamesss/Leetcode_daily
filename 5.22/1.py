# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root_val = preorder[0] # 根节点的值就是前序遍历序列的第一个元素
        root = TreeNode(root_val) # 构造根节点
        i = inorder.index(root_val) # 在中序遍历序列中找到根节点的位置
        # 递归构造左子树和右子树
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
