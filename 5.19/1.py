#https://leetcode.cn/problems/recover-binary-search-tree/submissions/
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            # 判断当前节点是否小于前一个节点，如果是则记录被交换的节点
            if node.val < self.prev.val:
                if not self.first: # 第一个被交换的节点
                    self.first = self.prev
                self.second = node # 第二个被交换的节点
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
