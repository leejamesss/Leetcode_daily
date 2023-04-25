# https://leetcode.cn/problems/validate-binary-search-tree/submissions/
#利用中序遍历数列，判断是不是上升的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None # 用于记录前一个节点的值
        
        def inorder(node):
            if not node:
                return []
            
            res = inorder(node.left)
            res.append(node.val)
            res += inorder(node.right)
            return res
        
        for val in inorder(root):
            if self.prev is not None and val <= self.prev:
                return False
            self.prev = val
            
        return True
