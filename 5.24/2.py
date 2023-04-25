# https://leetcode.cn/problems/balanced-binary-tree/
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: TreeNode) -> int:
            # 空树高度为0
            if not root:
                return 0
        
            # 返回左右子树中高度最大值加1
            return max(height(root.left), height(root.right)) + 1
    
        # 空树为平衡树
        if not root:
            return True
    
        # 根节点左右子树高度差小于等于1，并且左右子树都是平衡树
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
