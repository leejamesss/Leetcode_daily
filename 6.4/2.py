# https://leetcode.cn/problems/sum-root-to-leaf-numbers/submissions/

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0 # 初始化 res
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, node, curr_num):
        if not node: # 如果当前节点为空，直接返回
            return
        if not node.left and not node.right: # 如果当前节点是叶子节点，计算对应数字之和并加入 res
            self.res += curr_num * 10 + node.val
            return
        curr_num = curr_num * 10 + node.val # 更新路径上的数字
        # 递归遍历左右子节点，并将当前数字传递下去
        if node.left:
            self.dfs(node.left, curr_num)
        if node.right:
            self.dfs(node.right, curr_num)
