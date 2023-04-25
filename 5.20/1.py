# https://leetcode.cn/problems/symmetric-tree/
#递归
#判断左右子树为空的情况
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
        
        return isSymmetric(root.left, root.right) if root else True
