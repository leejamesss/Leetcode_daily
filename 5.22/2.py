# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1] # 根节点的值就是后序遍历序列的最后一个元素
        root = TreeNode(root_val) # 构造根节点
        i = inorder.index(root_val) # 在中序遍历序列中找到根节点的位置
        # 递归构造左子树和右子树
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
